import sys,argparseimport os,glob,reimport numpy as npimport pandas as pd#from GenomeData import *import matplotlib# matplotlib.use('Agg')import matplotlib.pyplot as pltmatplotlib.rcParams['font.size']=13matplotlib.rcParams["font.sans-serif"] = ["Arial", "Liberation Sans", "Bitstream Vera Sans"]matplotlib.rcParams["font.family"] = "sans-serif"import seaborn as snssns.set(font_scale=1)sns.set_style("whitegrid", {'axes.grid' : False})sns.set_style("ticks")from matplotlib_venn import venn3,venn2from scipy import statsimport warningswarnings.filterwarnings("ignore")def mark_pvalue(compr_pos,positions,box_vals):    s,p = stats.ttest_ind(box_vals[compr_pos[1]],box_vals[compr_pos[0]],nan_policy='omit')    # y, h, col = np.percentile(np.append(box_vals[compr_pos[0]],box_vals[compr_pos[1]]),98)*.99 ,1.05, 'k'    # y2 = np.percentile(np.append(box_vals[compr_pos[0]],box_vals[compr_pos[1]]),95)*0.99    x1,x2 = positions[compr_pos[0]],positions[compr_pos[1]]    # p_label='{:.1e}'.format(p)    # if p_label[-2]=='0':    #     p_label = p_label[:-2]+p_label[-1]    # if p>=0.05:    #     p_label = 'n.s.'        y = np.percentile(box_vals[compr_pos[0]],97.5)    if p<0.05 and s>0:        plt.text(x2, y, '*', ha='center', va='center_baseline', color='r',fontsize=27)        return s,pindir = 'f5_coBinding_CTCF_gain_potential'outdir = 'f6_coBinding_CTCF_gain_potential_figs'os.makedirs(outdir,exist_ok=True)# atac_file = '../../../f9_TF_condensates_V3/data/TCGA/tcga_atac.bed'# name_match = pd.read_excel('../../../f9_TF_condensates_V3/data/TCGA/TCGA-ATAC_SE_cancerType_match.xlsx',index_col=0)   # name_match = name_match.dropna()# clinical_dir = '../../..//f7_TF_condensates_test/f6_revised_TCGA_ATAC_cor_SE/f2_clinical_hicor_atac_peaks/f1_clinical_at_each_peak/f2_caseID_each_peak_vs_clinical/'p_thre = 0.05alpha = .7# selected_factors = {'MCF-7 top_TFBSCP':['ERG','ELK1','FOS'],#                     'MCF-7 top_zscored_TFBSCP':['ERG','JUND','ZNF143'],#                     'HCT-116 top_TFBSCP':['ELF1','JUND','SRF',],#                     'HCT-116 top_zscored_TFBSCP':['JUND','CEBPB','YY1']}selected_factors = {}tfbs_cp_dir = '../f2_cor_CP_SE_AICAP/f9_per_CT_TFBS_CP_cor_zscore_CP/TFBS_CP/'for ct in ['MCF-7','HCT-116'][:]:    df = pd.read_csv('{}/_CP_TFBS_all_vs_TFMS_{}.csv'.format(tfbs_cp_dir,ct),index_col=0)    selected_factors['{} top_TFBSCP'.format(ct)] = df['TFBS CP rank'].sort_values().iloc[:3].index    selected_factors['{} top_zscored_TFBSCP'.format(ct)] = df['avg rank'].sort_values().iloc[:3].index# flag = 'ATAC-seq peaks'for ct in ['MCF-7','HCT-116'][:]:# for cancertype in ['BRCA','COAD'][:]:    # ct = name_match.loc[cancertype].SE    # clinical_df = pd.read_csv('{}/{}_logrank_info.csv'.format(clinical_dir,cancertype),index_col=0)    for ctcf_type in ['diff_CTCF','diff_CTCF_specific_thre0.3']:        ctcf_file = 'data/BRCA_{}.bed'.format(ctcf_type) if ct== 'MCF-7' else 'data/CRC_{}.bed'.format(ctcf_type)    # ctcf_file = 'data/BRCA_diff_CTCF.bed' if ct== 'MCF-7' else 'data/CRC_diff_CTCF.bed'        for treat_flag in ['percentile_T','percentile_T_ExtendMerge'][:1]:            for factorType in ['top_TFBSCP','top_zscored_TFBSCP'][1:]:                # subdir = '{}_{}'.format(ct,factorType)                subdir = '{}_{}_{}'.format(ct,factorType,ctcf_type)                os.makedirs(outdir+os.sep+subdir,exist_ok=True)                            factors = selected_factors['{} {}'.format(ct,factorType)]                                xticklabels = ['Union',                               '{}'.format('-'.join([i for i in factors[:1]])),                               '{}'.format('-'.join([i for i in factors[1:2]])),                               '{}'.format('-'.join([i for i in factors[2:3]])),                               '{}'.format('-'.join([i for i in factors[:2]])),                               '{}'.format('-'.join([i for i in factors[:3]])),                               ]                                box_vals = []                # out_df = pd.DataFrame()                # overlapped_bed = '{}/{}/atac_overlapped_{}_{}_{}.bed'.format(indir,subdir,treat_flag,ct,xticklabels[ii])                df = pd.read_csv(ctcf_file,sep='\t',index_col=3,header=None)                df.columns = ['chr','start','end','id','score']                box_vals.append(df.score.values)                # add_logrank_info(out_df,clinical_df,'All',flag)                                # plt.figure(figsize=(3,2.5))                for ii in np.arange(len(xticklabels))[:]:                    overlapped_bed = '{}/{}/ctcf_overlapped_{}_{}_{}.bed'.format(indir,subdir,treat_flag,ct,xticklabels[ii])                    overlapped_df = pd.read_csv(overlapped_bed,sep='\t',index_col=3,header=None)                    overlapped_df.columns = ['chr','start','end','id','score']                    box_vals.append(overlapped_df.score.values)                    # sns.distplot(overlapped_df.score.values)                    # ==== save the clinical info                    # merged_df = pd.concat([overlapped_df,clinical_df],axis=1).dropna()                    # merged_df.to_csv('{}/{}/_{}_{}_{}_logRank.csv'.format(outdir,subdir,cancertype,treat_flag,xticklabels[ii]))                                       # clinical_df_tf = clinical_df.loc[overlapped_df.index]                    # add_logrank_info(out_df,clinical_df_tf,xticklabels[ii],'ATAC-seq peaks')                    # commandLine = 'bedtools intersect \\\n-a {} \\\n-b {} \\\n-wa -u > {}\n'.format(atac_file,outbed,overlapped_bed)                    # print(commandLine);os.system(commandLine)                            # out_df.to_csv('{}/{}/{}_{}_clinical.csv'.format(outdir,subdir,cancertype,treat_flag))                figname = '{}/{}/{}_{}.pdf'.format(outdir,subdir,ct,treat_flag)                # stack_bar(out_df,['All']+xticklabels,figname,cancertype,flag)                    positions = np.arange(7)                plt.figure(figsize=(3,2.5))                g = plt.boxplot(box_vals,positions=positions,widths = .6,patch_artist=True,\                            boxprops=dict(color='k',facecolor='w',fill=None,lw=1),\                            medianprops=dict(color='grey'),showfliers=False)                    # g = plt.violinplot(box_vals,positions=positions)                # scatter_X = []                # for position_id in np.arange(len(positions)):                #     scatter_x = np.random.normal(positions[position_id],0.07,len(box_vals[position_id]))                #     plt.scatter(scatter_x,box_vals[position_id],color='r',s=20,zorder=0,alpha=0.99,rasterized=True)                            out_df = pd.DataFrame()                for ii in [1,2,3,4,5,6]:                    s,p = mark_pvalue([0,ii,'t'],positions,box_vals)                    out_df.loc[xticklabels[ii-1],'ttest-s'] = s                    out_df.loc[xticklabels[ii-1],'ttest-p'] = p                                    plt.axes().set_xticklabels(['All']+xticklabels,fontsize=12,rotation=45,ha='right')                plt.axhline(y=0,color='k',lw=1.2,ls='--')                # plt.xlim([0,i+1])                # plt.ylim([-.1,7])                # plt.axes().set_xticks(positions+0.7)                # plt.axes().set_xticklabels(['< 20kb','20 - 100kb','> 100kb'],rotation=0, ha='right',fontsize=16,color='k')                # plt.legend([g["boxes"][0],g["boxes"][1],g["boxes"][2]],['Control','ENCODE','GTEx'],fontsize=16,borderaxespad=0.1,labelspacing=.1,handletextpad=0.2,loc="upper left",frameon=False)                # plt.axes().tick_params(axis='y',direction='out', length=4, width=1, colors='black')                    plt.ylabel('$\Delta$CTCF binding',fontsize=14)                plt.title('{}\n{}\n'.format(ct,ctcf_type))                plt.savefig(figname,bbox_inches='tight',                            pad_inches=0.1,dpi=600,transparent=True)                plt.show()                plt.close()                                out_df.to_csv('{}/{}/_{}_{}.csv'.format(outdir,subdir,ct,treat_flag))                                                                                                                        