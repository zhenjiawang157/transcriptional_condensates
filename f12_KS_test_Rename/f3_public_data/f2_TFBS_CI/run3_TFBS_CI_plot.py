import sys,argparse
import os,glob,re
import numpy as np
import pandas as pd
#from GenomeData import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams['font.size']=14
matplotlib.rcParams["font.sans-serif"] = ["Arial", "Liberation Sans", "Bitstream Vera Sans"]
matplotlib.rcParams["font.family"] = "sans-serif"
import seaborn as sns
sns.set(font_scale=1.1)
sns.set_style("whitegrid", {'axes.grid' : False})
sns.set_style("ticks")
# from matplotlib_venn import venn3,venn2
from scipy import stats
import warnings
warnings.filterwarnings("ignore")


def get_lines(infile):

    with open(infile,'rb') as f:
        lines = 0
        buf_size = 1024*1024
        buf = f.raw.read(buf_size)
        while buf:
            lines += buf.count(b'\n')
            buf = f.raw.read(buf_size)
    return lines


def mark_pvalue(compr_pos,positions,box_vals):
    s,p = stats.ttest_ind(box_vals[compr_pos[1]],box_vals[compr_pos[0]],nan_policy='omit')
    y, h, col = np.percentile(np.append(box_vals[compr_pos[0]],box_vals[compr_pos[1]]),91)*0.95 ,1.1, 'k'
    y2 = np.percentile(np.append(box_vals[compr_pos[0]],box_vals[compr_pos[1]]),0)*0.9
    # x1,x2 = positions[compr_pos[0]],positions[compr_pos[1]]
    x1,x2 = positions[int(compr_pos[0]/2)]-.2, positions[int(compr_pos[0]/2)]+.2
    # p_label='{} {:.1e}'.format('dn' if s>0 else 'up', p)
    p_label='{:.1e}'.format(p)
    if p_label[-2]=='0':
        p_label = p_label[:-2]+p_label[-1]
    # if p<1:
    if p<0.05 and s>0:
        if p>0.05:
            p_label = 'n.s.'
        if compr_pos[2] == 't':
            plt.plot([x1+.03, x1+.03, x2-.03, x2-.03], [y, y*h, y*h, y], lw=1, c=col)
            plt.text((x1+x2)*.5, y*1.2, '*', ha='center', va='center', color='red',fontsize=33)
        else:
            plt.plot([x1*1.03, x1*1.03, x2*0.97, x2*0.97], [y2, y2*1.1, y2*1.1, y2], lw=1, c=col)
            plt.text((x1+x2)*.5, y2*1.25, p_label, ha='center', va='top', color=col,fontsize=13)
    return s,p




# ==== main 
indir = 'f2_CI_intersect_TFBS'
outdir = 'f3_CI_figs'
os.makedirs(outdir,exist_ok=True)

tfbs_dir = '../../f1_TF_cluster_potential/f2_cor_CP_SE_AICAP/f3_TFBS_CP_heatmap_with_motif_SE//_csv/'
tfbs_cp_s = pd.read_csv('{}/data_fisher_CP_TFBS_all_vs_TFMS_CP_KStest_statistics.csv'.format(tfbs_dir),index_col=0)
rank_dir = '../../f1_TF_cluster_potential/f2_cor_CP_SE_AICAP/f9_per_CT_TFBS_CP_cor_zscore_CP_with_motif_SE/TFBS_CP/'
merge_file_dir = '../../f1_TF_cluster_potential/f3_clustered_TFBS/f2_bedfiles_merged'

cts = ['MCF-7','HCT-116','HeLa','LNCaP','U87','HepG2']
cellTypes = ['LNCaP','H1','HepG2','MCF7','Panc1','GM12878','HeLa','IMR90','K562','HCT116','Jurkat']
genomic_KB_distances = [20,50,100,200,500]
treat_flags =['percentile_T','percentile_T_ExtendMerge']

for treat_flag in treat_flags:
    for genomic_KB_distance in genomic_KB_distances[:]:
        for ct in cts[:]:
            ct_rename = ''.join(ct.split('-'))
            if not ct_rename in cellTypes:
                continue
    
            rank_df = pd.read_csv('{}/_CP_TFBS_all_vs_TFMS_{}.csv'.format(rank_dir,ct),index_col=0)
            factors = rank_df.index
            factors = [i for i in factors if i in tfbs_cp_s[ct].dropna().index[:]]
            # factors = tfbs_cp_s[ct].dropna().index[:]
            
            outdf = pd.DataFrame()
            box_vals_T = []
            box_vals_C = []
            box_vals = []
            
            for factor in factors: 
                infile_t = '{}/{}/{}_{}_percentile_T_overlap_CI_{}KB.bed'.format(indir,ct_rename,ct_rename,factor,genomic_KB_distance)
                infile_c = '{}/{}/{}_{}_percentile_C_overlap_CI_{}KB.bed'.format(indir,ct_rename,ct_rename,factor,genomic_KB_distance)
                                        
                if os.path.isfile(infile_t) and get_lines(infile_t)>0:
                    df_C = pd.read_csv(infile_c,header=None,sep='\t')    
                    df_C = df_C.iloc[:,3:]
                    val = np.concatenate(df_C.values)
                    val = val[val!=0]
                    val = val[~np.isnan(val)]
                    box_vals_C.append(val)
                    box_vals.append(val)
            
                    
                    df_T = pd.read_csv(infile_t,header=None,sep='\t')  
                    df_T = df_T.iloc[:,3:]
                    val = np.concatenate(df_T.values)
                    val = val[val!=0]
                    val = val[~np.isnan(val)]
                    box_vals_T.append(val)
                    box_vals.append(val)
                    print(ct,factor)
    
             
            if not len(box_vals_T) == len(box_vals_C):
                print(ct,factor,genomic_KB_distance)
                continue
                                        
            positions = np.arange(len(box_vals_T))
            print(ct,factor,genomic_KB_distance)
            print(len(box_vals_T),len(box_vals_C),len(positions))     
            
            plt.figure(figsize=(len(box_vals_T),2.6))
            
            g1 = plt.boxplot(box_vals_C,positions=positions-.2,widths =.3,patch_artist=True,\
                        boxprops=dict(color='k',facecolor='silver',fill=True,lw=1),\
                        medianprops=dict(color='k'),showfliers=False)
            
            g2 = plt.boxplot(box_vals_T,positions=positions+.2,widths =.3,patch_artist=True,\
                        boxprops=dict(color='k',facecolor='r',fill=True,lw=1),\
                        medianprops=dict(color='k'),showfliers=False)
                
            # scatter_X = []
            # for position_id in np.arange(len(positions)):
            #     scatter_x = np.random.normal(positions[position_id],0.05,len(box_vals[position_id]))
            #     plt.scatter(scatter_x,box_vals[position_id],color=colors[position_id],
            #                 lw=0,s=22,zorder=0,alpha=.5,marker='o',rasterized=True)
            
            factor_ii=0
            for compr_pos in [[ii,ii+1,'t'] for ii in positions*2]:
                s,p = mark_pvalue(compr_pos,positions,box_vals)
                outdf.loc[factors[factor_ii],'statistics'] = s
                outdf.loc[factors[factor_ii],'pvalue'] = p
                factor_ii+=1
                
            
            plt.title(ct)
            plt.ylabel('Chromatin interaction ({}Kb)'.format(genomic_KB_distance))
            plt.xlim([-.5,len(box_vals_T)-.5])
            plt.axes().set_xticks(positions)
            plt.axes().set_xticklabels(factors,rotation=60,ha='right',fontsize=14)
            plt.axhline(y=0,color='grey',linestyle='--',linewidth=.7)
            
            plt.legend([g1["boxes"][0],g2["boxes"][0]],['NC-TFBS','C-TFBS'],bbox_to_anchor=[1.,1.3], 
                        markerscale=1.5,fontsize=13,borderaxespad=0.2,labelspacing=.2,
                        handletextpad=0.2,handlelength=1,loc="upper right",frameon=False)
            
            prename = '{}_{}_CI_{}KB'.format(ct,treat_flag,genomic_KB_distance)
            plt.savefig('{}/{}.pdf'.format(outdir,prename),
                        bbox_inches='tight',pad_inches=0.1,dpi=600,transparent=True)
            plt.show()
            plt.close()
            
            outdf.to_csv('{}/_{}.csv'.format(outdir,prename),)
    



