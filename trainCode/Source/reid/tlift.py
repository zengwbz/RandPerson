import numpy as np
import math

def TLift(in_score, gal_cam_id, gal_time, prob_cam_id, prob_time, num_cams, tau, sigma, K, alpha=0.1):
    '''Function for the Temporal Lifting (TLift) method
    TLift is a model-free temporal cooccurrence based score weighting method proposed in
    "Interpretable and Generalizable Deep Image Matching with Query-adaptive Convolutions".
    Inputs:
        in_score: the similarity score of size [num_probs, num_gals] between the gallery and probe sets.
        gal_cam_id: camera index for samples in the gallery set.
        gal_time: time stamps of samples in the gallery set.
        prob_cam_id: camera index for samples in the probe set.
        prob_time: time stamps of samples in the probe set.
        num_cams: the number of cameras.
        tau: the interval threshold to define nearby persons.
        sigma: the sensitivity parameter of the time difference.
        K: parameter of the top K retrievals used to define the pivot set P.
        All the cam_id and time inputs are column vectors, and they are in the same order corresponding to
        rows (probe) or columns (gallery) of the in_score.
    Outputs:
        out_score: the refined score by TLift, with the same size as the in_score.
    '''
    out_score = np.zeros_like(in_score)
    if len(prob_time.shape) == 1:
        prob_time = prob_time[np.newaxis, :]
    prob_time_diff = prob_time - np.transpose(prob_time)
    cooccur_mask = (abs(prob_time_diff) < tau)
    g_sam_index = []
    score = []
    gal_time_diff = []

    for g_cam in range(num_cams):
        g_sam_index.append(np.where(gal_cam_id == g_cam)[0])  # camera id start with 0/1.
        score.append(in_score[:, g_sam_index[g_cam]])
        frame_id = gal_time[g_sam_index[g_cam]]
        if len(frame_id.shape) == 1:
            frame_id = frame_id[np.newaxis, :]
        gal_time_diff.append(frame_id - np.transpose(frame_id))

    for p_cam in range(num_cams):
        p_sam_index = np.where(prob_cam_id == p_cam)[0]
        c_mask = cooccur_mask[p_sam_index][:, p_sam_index]
        num_prob = len(p_sam_index)
        for g_cam in range(num_cams):
            # if p_cam == g_cam:  # in some public datasets they still evaluate negative pairs in the same camera
            #     continue
            prob_score = score[g_cam][p_sam_index, :]
            for i in range(num_prob):
                cooccur_index = np.where(c_mask[:, i] == True)[0]
                cooccur_score = prob_score[cooccur_index, :]
                thr = np.sort(cooccur_score, axis=None)[-K]
                mask_in_gal = np.where(cooccur_score >= thr)[1]
                dt = gal_time_diff[g_cam][:, mask_in_gal]
                weight = np.mean(np.exp(-1 * np.true_divide(np.square(dt), math.pow(sigma, 2))), axis=1)
                #tmp = prob_score[:, i]
                out_score[p_sam_index[i], g_sam_index[g_cam]] = weight  #* prob_score[:, i]

    # out_score = np.true_divide(out_score - out_score.min(), out_score.max() - out_score.min())
    # in_score = np.true_divide(in_score - in_score.min(), in_score.max() - in_score.min())
    # out_score = out_score + alpha * in_score
    out_score = (out_score + alpha) * in_score
    return out_score


if __name__ == '__main__':
    in_score = np.random.randn(100,50)
    gal_cam_id = np.random.randint(0, 5, (100))
    gal_time = np.random.randint(0, 20, (100))
    prob_cam_id = np.random.randint(0, 5, (50))
    prob_time = np.random.randint(0, 20, (50))
    num_cams = 5
    tau = 4
    sigma = 10
    K = 10
    TLift(in_score, gal_cam_id, gal_time, prob_cam_id, prob_time, num_cams, tau,
          sigma, K)