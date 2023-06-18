import sys,argparseimport os,glob,reimport numpy as npimport pandas as pd#from GenomeData import *import matplotlib# matplotlib.use('Agg')import matplotlib.pyplot as pltmatplotlib.rcParams['font.size']=13matplotlib.rcParams["font.sans-serif"] = ["Arial", "Liberation Sans", "Bitstream Vera Sans"]matplotlib.rcParams["font.family"] = "sans-serif"import seaborn as snssns.set(font_scale=1)sns.set_style("whitegrid", {'axes.grid' : False})sns.set_style("ticks")# from matplotlib_venn import venn3,venn2from scipy import statsimport warningswarnings.filterwarnings("ignore")def get_lines(infile):    with open(infile,'rb') as f:        lines = 0        buf_size = 1024*1024        buf = f.raw.read(buf_size)        while buf:            lines += buf.count(b'\n')            buf = f.raw.read(buf_size)    return linesdef mark_pvalue(compr_pos,positions,box_vals):    s,p = stats.ttest_ind(box_vals[compr_pos[1]],box_vals[compr_pos[0]],nan_policy='omit')    y, h, col = np.percentile(np.append(box_vals[compr_pos[0]],box_vals[compr_pos[1]]),91)*0.95 ,1.1, 'k'    y2 = np.percentile(np.append(box_vals[compr_pos[0]],box_vals[compr_pos[1]]),0)*0.9    # x1,x2 = positions[compr_pos[0]],positions[compr_pos[1]]    x1,x2 = positions[int(compr_pos[0]/2)]-.2, positions[int(compr_pos[0]/2)]+.2    # p_label='{} {:.1e}'.format('dn' if s>0 else 'up', p)    p_label='{:.1e}'.format(p)    if p_label[-2]=='0':        p_label = p_label[:-2]+p_label[-1]    # if p<1:    if p<0.05 and s>0:        if p>0.05:            p_label = 'n.s.'        if compr_pos[2] == 't':            plt.plot([x1+.03, x1+.03, x2-.03, x2-.03], [y, y*h, y*h, y], lw=1, c=col)            plt.text((x1+x2)*.5, y*1.2, '*', ha='center', va='center', color='red',fontsize=33)        else:            plt.plot([x1*1.03, x1*1.03, x2*0.97, x2*0.97], [y2, y2*1.1, y2*1.1, y2], lw=1, c=col)            plt.text((x1+x2)*.5, y2*1.25, p_label, ha='center', va='top', color=col,fontsize=13)    return s,pindir='f3_avg_RP_per_sample_across_patients'outdir = 'f4_avg_RP_per_sample_across_patients_figs'os.makedirs(outdir,exist_ok=True)tfbs_dir = '../../..//f1_TF_cluster_potential/f2_cor_CP_SE_AICAP/f3_TFBS_CP_heatmap//_csv/'tfbs_cp_s = pd.read_csv('{}/data_fisher_CP_TFBS_vs_TFMS_CP_RankSum_statistics.csv'.format(tfbs_dir),index_col=0)name_match = pd.read_excel('../../../data/TCGA/TCGA-ATAC_SE_cancerType_match.xlsx',index_col=0)   name_match = name_match.dropna()treat_flags = ['percentile_T.merge','percentile_T_ExtendMerge.merge']alpha = .7halflifes = [10000,5000,20000]for halflife in halflifes[:]:    for flag in treat_flags[:]:        for cancertype in ['BRCA', 'CESC', 'COAD', 'LIHC', 'PRAD'][:]:            ct = name_match.loc[cancertype,'SE']            factors = tfbs_cp_s[ct].dropna().sort_values(ascending=False).index                          outdf = pd.DataFrame()            box_vals_T = []            box_vals_C = []            box_vals = []                        for factor in factors[:]:                 print(halflife, flag, cancertype, factor)                infile_t = '{}/{}/{}_avg_RP_halflife_{}_on_{}_{}_{}.csv'.format(indir,cancertype,cancertype,halflife,ct,factor,flag)                infile_c = '{}/{}/{}_avg_RP_halflife_{}_on_{}_{}_percentile_C.merge.csv'.format(indir,cancertype,cancertype,halflife,ct,factor)                if get_lines(infile_t)>0:                    df_C = pd.read_csv(infile_c,header=None,index_col=0)                        val = df_C[1].values                    box_vals_C.append(val)                    box_vals.append(val)                                df_T = pd.read_csv(infile_t,header=None,index_col=0)                        val = df_T[1].values                    box_vals_T.append(val)                    box_vals.append(val)                                positions = np.arange(len(box_vals_T))            plt.figure(figsize=(len(box_vals_T),2.6))                g1 = plt.boxplot(box_vals_C,positions=positions-.2,widths =.3,patch_artist=True,\                        boxprops=dict(color='k',facecolor='silver',fill=True,lw=1),\                        medianprops=dict(color='k'),showfliers=False)                g2 = plt.boxplot(box_vals_T,positions=positions+.2,widths =.3,patch_artist=True,\                        boxprops=dict(color='k',facecolor='r',fill=True,lw=1),\                        medianprops=dict(color='k'),showfliers=False)                            # scatter_X = []            # for position_id in np.arange(len(positions)):            #     scatter_x = np.random.normal(positions[position_id],0.05,len(box_vals[position_id]))            #     plt.scatter(scatter_x,box_vals[position_id],color=colors[position_id],            #                 lw=0,s=22,zorder=0,alpha=.5,marker='o',rasterized=True)                        factor_ii=0            for compr_pos in [[ii,ii+1,'t'] for ii in positions*2]:                s,p = mark_pvalue(compr_pos,positions,box_vals)                outdf.loc[factors[factor_ii],'statistics'] = s                outdf.loc[factors[factor_ii],'pvalue'] = p                factor_ii+=1                # print(cancertype,flag,compr_pos,s,p)                        plt.title(cancertype)            plt.ylabel('{} ATAC-seq RP'.format(cancertype))            plt.xlim([-.5,len(box_vals_T)-.5])            plt.axes().set_xticks(positions)            plt.axes().set_xticklabels(factors,rotation=60,ha='right',fontsize=16)            plt.axhline(y=0,color='grey',linestyle='--',linewidth=.7)                        plt.legend([g1["boxes"][0],g2["boxes"][0]],['Control','Clustered'],bbox_to_anchor=[1.,1.3],                        markerscale=1.5,fontsize=13,borderaxespad=0.2,labelspacing=.2,                       handletextpad=0.2,handlelength=1,loc="upper right",frameon=False)            plt.title(ct)            plt.savefig('{}/{}_halflife_{}_by_{}.pdf'.format(outdir,cancertype,halflife,flag),                        bbox_inches='tight',pad_inches=0.1,dpi=600,transparent=True)            plt.show()            plt.close()                        outdf.to_csv('{}/{}_halflife_{}_by_{}.csv'.format(outdir,cancertype,halflife,flag),)        