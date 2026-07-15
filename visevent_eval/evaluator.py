import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib

def config_tracker():
    trackers = [
        {'name': 'CN(MF)'}, {'name': 'CSK(MF)'}, {'name': 'DAT(MF)'}, {'name': 'KCF(MF)'},
        {'name': 'LDES(MF)'}, {'name': 'MANet(MF)'}, {'name': 'MOSSE(MF)'}, {'name': 'ATOM(EF)'},
        {'name': 'MDNet(MF)'}, {'name': 'MetaTracker(MF)'}, {'name': 'RTMDNet(MF)'}, {'name': 'SiamFC(MF)'},
        {'name': 'SiamMask(EF)'}, {'name': 'SiamRPN(EF)'}, {'name': 'SiamRPNppLT(ResNet50)(EF)'},
        {'name': 'SiamRPNpp(AlexNet)(EF)'}, {'name': 'SiamRPNpp(ResNet50)(EF)'}, {'name': 'STRCF(MF)'},
        {'name': 'VITAL(MF)'}, {'name': 'DIMP18(EF)'}, {'name': 'SuperDIMP(EF)'}, {'name': 'PrDIMP18(EF)'},
        {'name': 'DIMP50(EF)'}, {'name': 'PrDIMP50(EF)'}, {'name': 'Ours-MDNet(MF)'}, {'name': 'Ours-RTMDNet(MF)'},
        {'name': 'Ocean(EF)'}, {'name': 'SiamDW(EF)'}, {'name': 'SiamCAR(EF)'}, {'name': 'TADT(EF)'},
        {'name': 'UDT(EF)'}, {'name': 'SiamKPN(EF)'}, {'name': 'DaSiamRPN(EF)'}, {'name': 'CLNet(EF)'},
        {'name': 'SiamBAN(EF)'}, {'name': 'RTAA(EF)'}, {'name': 'FCOT(EF)'}, {'name': 'ROAM(EF)'},
        {'name': 'SiamRCNN(EF)'}, {'name': 'GradNet(EF)'}, {'name': 'TACT(EF)'}, {'name': 'LTMU(EF)'}, {'name': 'XTrack-B'}, {'name': 'XTrack-L'}, {'name': 'FlexTrack'}
    ]
    return trackers

def config_plot_style():
    plot_styles = [
        {'color': (1,0,0),          'lineStyle': '-'},
        {'color': (0,1,0),          'lineStyle': '-'},
        {'color': (0,0,1),          'lineStyle': '-'},
        {'color': (0,0,0),          'lineStyle': '-'},
        {'color': (1,0,1),          'lineStyle': '-'},
        {'color': (0,1,1),          'lineStyle': '-'},
        {'color': (0.5,0.5,0.5),    'lineStyle': '-'},
        {'color': (136/255,0,21/255),   'lineStyle': '-'},
        {'color': (255/255,127/255,39/255), 'lineStyle': '-'},
        {'color': (0,162/255,232/255),  'lineStyle': '-'},
        {'color': (163/255,73/255,164/255), 'lineStyle': '-'},
        {'color': (191/255,144/255,0),  'lineStyle': '-'},
        {'color': (1,0,0),          'lineStyle': '--'},
        {'color': (0,1,0),          'lineStyle': '--'},
        {'color': (0,0,1),          'lineStyle': '--'},
        {'color': (0,0,0),          'lineStyle': '--'},
        {'color': (1,0,1),          'lineStyle': '--'},
        {'color': (0,1,1),          'lineStyle': '--'},
        {'color': (0.5,0.5,0.5),    'lineStyle': '--'},
        {'color': (136/255,0,21/255),   'lineStyle': '--'},
        {'color': (255/255,127/255,39/255), 'lineStyle': '--'},
        {'color': (0,162/255,232/255),  'lineStyle': '--'},
        {'color': (163/255,73/255,164/255), 'lineStyle': '--'},
        {'color': (191/255,144/255,0),  'lineStyle': '--'},
        {'color': (1,0,0),          'lineStyle': '-.'},
        {'color': (0,1,0),          'lineStyle': '-.'},
        {'color': (0,0,1),          'lineStyle': '-.'},
        {'color': (0,0,0),          'lineStyle': '-.'},
        {'color': (1,0,1),          'lineStyle': '-.'},
        {'color': (0,1,1),          'lineStyle': '-.'},
        {'color': (0.5,0.5,0.5),    'lineStyle': '-.'},
        {'color': (136/255,0,21/255),   'lineStyle': '-.'},
        {'color': (255/255,127/255,39/255), 'lineStyle': '-.'},
        {'color': (0,162/255,232/255),  'lineStyle': '-.'},
        {'color': (163/255,73/255,164/255), 'lineStyle': '-.'},
        {'color': (191/255,144/255,0),  'lineStyle': '--'},
        {'color': (191/255,50/255,0),  'lineStyle': '--'},
        {'color': (191/255,10/255,0),  'lineStyle': '--'},
        {'color': (100/255,144/255,0),  'lineStyle': '--'},
        {'color': (191/255,144/255,190/255),  'lineStyle': '-.'},
        {'color': (191/255,144/255,100/255),  'lineStyle': '-.'},
        {'color': (255/255,144/255,255/255),  'lineStyle': '-.'},
        {'color': (191/255,144/255,30/255),  'lineStyle': '-.'}
    ]
    return plot_styles

def config_sequence(eval_type):
    if eval_type == 'test_set':
        dataset_name = os.path.join(os.path.dirname(__file__), 'sequence_evaluation_config', 'VisEvent_testing_subset.txt')
    else:
        raise ValueError("Error in evaluation dataset type!")
        
    with open(dataset_name, 'r') as f:
        sequences = [line.strip() for line in f.readlines() if line.strip()]
    return sequences

def calc_rect_int(A, B):
    leftA   = A[:,0]
    bottomA = A[:,1]
    rightA  = leftA + A[:,2] - 1
    topA    = bottomA + A[:,3] - 1

    leftB   = B[:,0]
    bottomB = B[:,1]
    rightB  = leftB + B[:,2] - 1
    topB    = bottomB + B[:,3] - 1

    tmp     = np.maximum(0, np.minimum(rightA, rightB) - np.maximum(leftA, leftB) + 1) * \
              np.maximum(0, np.minimum(topA, topB) - np.maximum(bottomA, bottomB) + 1)
    areaA   = A[:,2] * A[:,3]
    areaB   = B[:,2] * B[:,3]
    overlap = tmp / (areaA + areaB - tmp + 1e-16)
    return overlap

def calc_seq_err_robust(results, rect_anno, absent_anno, norm_dst):
    seq_length = rect_anno.shape[0]

    if results.shape[0] != rect_anno.shape[0]:
        results = results[:rect_anno.shape[0], :]

    for i in range(1, seq_length):
        r = results[i, :]
        r_anno = rect_anno[i, :]
        
        if (np.isnan(r).any() or r[2] <= 0 or r[3] <= 0) and not np.isnan(r_anno).any():
            results[i, :] = results[i-1, :]

    rect_mat = np.copy(results)
    rect_mat[0, :] = rect_anno[0, :]  

    absent_idx = (absent_anno == 1).flatten()
    valid_idx = ~absent_idx
    rect_mat = rect_mat[valid_idx, :]
    rect_anno = rect_anno[valid_idx, :]

    center_GT = np.column_stack([
        rect_anno[:, 0] + (rect_anno[:, 2] - 1) / 2,
        rect_anno[:, 1] + (rect_anno[:, 3] - 1) / 2
    ])

    center = np.column_stack([
        rect_mat[:, 0] + (rect_mat[:, 2] - 1) / 2,
        rect_mat[:, 1] + (rect_mat[:, 3] - 1) / 2
    ])

    new_seq_length = rect_anno.shape[0]

    if norm_dst:
        center[:, 0] = center[:, 0] / rect_anno[:, 2]
        center[:, 1] = center[:, 1] / rect_anno[:, 3]
        center_GT[:, 0] = center_GT[:, 0] / rect_anno[:, 2]
        center_GT[:, 1] = center_GT[:, 1] / rect_anno[:, 3]

    err_center = np.sqrt(np.sum((center[:new_seq_length, :] - center_GT[:new_seq_length, :])**2, axis=1))

    index = rect_anno > 0
    idx = np.sum(index, axis=1) == 4

    errCoverage = -np.ones(len(idx))
    if np.sum(idx) > 0:
        tmp = calc_rect_int(rect_mat[idx, :], rect_anno[idx, :])
        errCoverage[idx] = tmp
    err_center[~idx] = -1

    return errCoverage, err_center

def eval_tracker(seqs, trackers, eval_type, name_tracker_all, tmp_mat_path, path_anno, rp_all, norm_dst):
    num_tracker = len(trackers)

    threshold_set_overlap = np.arange(0, 1.05, 0.05)
    threshold_set_error = np.arange(0, 51)
    if norm_dst:
        threshold_set_error = threshold_set_error / 100.0 

    ave_success_rate_plot = np.zeros((num_tracker, len(seqs), len(threshold_set_overlap)))
    ave_success_rate_plot_err = np.zeros((num_tracker, len(seqs), len(threshold_set_error)))

    for i, s in enumerate(seqs):
        anno_file = os.path.join(path_anno, 'gt_rect', s + '.txt')
        absent_file = os.path.join(path_anno, 'absent', s + '.txt')

        anno = np.loadtxt(anno_file, delimiter=',') 
        absent_anno = np.loadtxt(absent_file)

        for k, t in enumerate(trackers):
            res_file1 = os.path.join(rp_all, t['name'] + '_tracking_result', s + '.txt')
            res_file2 = os.path.join(rp_all, t['name'] + '_tracking_result', 'results' + s + '.txt')
            res_file3 = os.path.join(rp_all, t['name'] + '_tracking_result', s + '_001.txt')
            
            res = None
            for r_file in [res_file1, res_file2, res_file3]:
                if os.path.exists(r_file):
                    try:
                        res = np.loadtxt(r_file, delimiter=',')
                    except:
                        try:
                            res = np.loadtxt(r_file)
                        except:
                            pass
                    if res is not None:
                        break

            success_num_overlap = np.zeros(len(threshold_set_overlap))
            success_num_err = np.zeros(len(threshold_set_error))

            if res is None or len(res) == 0:
                pass
            else:
                err_coverage, err_center = calc_seq_err_robust(res, anno, absent_anno, norm_dst)
                
                for t_idx, th in enumerate(threshold_set_overlap):
                    success_num_overlap[t_idx] = np.sum(err_coverage > th)
                
                for t_idx, th in enumerate(threshold_set_error):
                    success_num_err[t_idx] = np.sum(err_center <= th)

            len_all = anno.shape[0]

            eps = np.finfo(float).eps
            ave_success_rate_plot[k, i, :] = success_num_overlap / (len_all + eps)
            ave_success_rate_plot_err[k, i, :] = success_num_err / (len_all + eps)

    if not os.path.exists(tmp_mat_path):
        os.makedirs(tmp_mat_path)

    dataName1 = os.path.join(tmp_mat_path, f'aveSuccessRatePlot_{num_tracker}alg_overlap_{eval_type}.npz')
    np.savez(dataName1, ave_success_rate_plot=ave_success_rate_plot, name_tracker_all=name_tracker_all)

    dataName2 = os.path.join(tmp_mat_path, f'aveSuccessRatePlot_{num_tracker}alg_error_{eval_type}.npz')
    np.savez(dataName2, ave_success_rate_plot=ave_success_rate_plot_err, name_tracker_all=name_tracker_all)


def plot_draw_save(num_tracker, ave_success_rate_plot, idx_seq_set, rank_num, ranking_type, rank_idx,
                   name_tracker_all, threshold_set, title_name, x_label_name, y_label_name, fig_name, save_fig_path):
    plot_styles = config_plot_style()
    perf = np.zeros(num_tracker)
    for i in range(num_tracker):
        tmp = ave_success_rate_plot[i, idx_seq_set, :]
        row_sums = np.sum(tmp, axis=1)
        aa = tmp[row_sums > np.finfo(float).eps, :]
        if aa.shape[0] > 0:
            bb = np.mean(aa, axis=0)
            if ranking_type == 'AUC':
                perf[i] = np.mean(bb)
            elif ranking_type == 'threshold':
                perf[i] = bb[rank_idx]
        else:
            perf[i] = 0

    index_sort = np.argsort(perf)[::-1]
    
    # Matching MATLAB plot settings
    plt.rc('font', size=14)
    plt.rc('axes', titlesize=14)
    plt.rc('axes', labelsize=14)
    plt.rc('xtick', labelsize=14)
    plt.rc('ytick', labelsize=14)
    plt.rc('legend', fontsize=12)
    
    fig, ax = plt.subplots(figsize=(8, 7))
    
    for i, k in enumerate(index_sort[:rank_num]):
        tmp = ave_success_rate_plot[k, idx_seq_set, :]
        row_sums = np.sum(tmp, axis=1)
        aa = tmp[row_sums > np.finfo(float).eps, :]
        
        if aa.shape[0] > 0:
            bb = np.mean(aa, axis=0)
        else:
            bb = np.zeros_like(threshold_set)
            
        if ranking_type == 'AUC':
            score = np.mean(bb)
            label = f'[{score:.3f}] {name_tracker_all[k]}'
        else:
            score = bb[rank_idx]
            label = f'[{score:.3f}] {name_tracker_all[k]}'
            
        style = plot_styles[i % len(plot_styles)]
        
        ax.plot(threshold_set, bb, label=label, linewidth=4, 
                 color=style['color'], linestyle=style['lineStyle'])

    if ranking_type == 'threshold':
        ax.legend(loc='upper left', fontsize=12)
        ax.set_xlim([0, 50])
    else:
        ax.legend(loc='upper right', fontsize=12)
        ax.set_xlim([0, 1])
        
    ax.set_ylim([0, 0.85])
    # In MATLAB screenshot, precision plot has ticks roughly 0, 5, 10, ...
    
    # MATLAB grid styling: 'GridLineStyle', ':', 'GridColor', 'k', 'GridAlpha', 1, 'LineWidth', 1.2
    ax.grid(True, linestyle=':', color='k', alpha=1.0, linewidth=1.2)
        
    ax.set_title(title_name)
    ax.set_xlabel(x_label_name)
    ax.set_ylabel(y_label_name)
    
    if not os.path.exists(save_fig_path):
        os.makedirs(save_fig_path)
    
    plt.tight_layout()
    plt.savefig(os.path.join(save_fig_path, fig_name + '.png'), dpi=300)
    plt.close()

import argparse
import os

DEFAULT_ANNO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'annos')

def main():
    parser = argparse.ArgumentParser(description="Evaluate VisEvent Trackers.")
    parser.add_argument("--tracking_results", type=str, default="./tracking_results", help="Path to your trackers results folder")
    parser.add_argument("--annos", type=str, default=DEFAULT_ANNO_DIR, help="Path to VisEvent annos folder (defaults to built-in)")
    parser.add_argument("--tmp_mat", type=str, default="./tmp_mat", help="Path to save intermediate .npz files")
    parser.add_argument("--res_fig", type=str, default="./res_fig", help="Path to save plot figures")
    args = parser.parse_args()
    tmp_mat_path = args.tmp_mat
    path_anno = args.annos
    rp_all = args.tracking_results
    save_fig_path = args.res_fig
    
    evaluation_dataset_type = 'test_set'
    norm_dst = False

    trackers = config_tracker()
    if os.path.exists(rp_all):
        found_trackers = []
        for d in os.listdir(rp_all):
            if os.path.isdir(os.path.join(rp_all, d)) and d.endswith("_tracking_result"):
                found_trackers.append({"name": d.replace("_tracking_result", "")})
        if found_trackers:
            trackers = found_trackers
    sequences = config_sequence(evaluation_dataset_type)

    name_tracker_all = [t['name'] for t in trackers]

    eval_type = 'OPE'
    
    print("Evaluating trackers...")
    eval_tracker(sequences, trackers, eval_type, name_tracker_all, tmp_mat_path, path_anno, rp_all, norm_dst)
    
    num_tracker = len(trackers)
    idx_seq_set = list(range(len(sequences)))
    rank_num = 50
    if rank_num > num_tracker:
        rank_num = num_tracker

    metric_type_set = ['error', 'overlap']
    
    for metric_type in metric_type_set:
        if metric_type == 'error':
            threshold_set = np.arange(0, 51)
            if norm_dst:
                threshold_set = threshold_set / 100.0
            rank_idx = 20 # index 20 is threshold 20
            x_label_name = 'Location error threshold'
            y_label_name = 'Precision'
            ranking_type = 'threshold'
            title_name = 'Precision plots of ' + eval_type
            if norm_dst:
                title_name = 'Normalized ' + title_name
            title_name += ' on VisEvent Testing Set'
            
            dataName = os.path.join(tmp_mat_path, f'aveSuccessRatePlot_{num_tracker}alg_error_{eval_type}.npz')
            plot_type = f'error_{eval_type}'
            
        elif metric_type == 'overlap':
            threshold_set = np.arange(0, 1.05, 0.05)
            rank_idx = 10 # index 10 is threshold 0.5
            x_label_name = 'Overlap threshold'
            y_label_name = 'Success rate'
            ranking_type = 'AUC'
            title_name = 'Success plots of ' + eval_type + ' on VisEvent Testing Set'
            
            dataName = os.path.join(tmp_mat_path, f'aveSuccessRatePlot_{num_tracker}alg_overlap_{eval_type}.npz')
            plot_type = f'overlap_{eval_type}'

        if os.path.exists(dataName):
            data = np.load(dataName)
            ave_success_rate_plot = data['ave_success_rate_plot']
            fig_name = f'{plot_type}_{ranking_type}'
            
            plot_draw_save(num_tracker, ave_success_rate_plot, idx_seq_set, rank_num, ranking_type, rank_idx,
                           name_tracker_all, threshold_set, title_name, x_label_name, y_label_name, fig_name, save_fig_path)
            print(f"Saved {fig_name}.png to {save_fig_path}")

if __name__ == '__main__':
    main()
