import sys,argparseimport os,glob,reimport numpy as npimport pandas as pd#from GenomeData import *import matplotlib# matplotlib.use('Agg')import matplotlib.pyplot as pltmatplotlib.rcParams['font.size']=13matplotlib.rcParams["font.sans-serif"] = ["Arial", "Liberation Sans", "Bitstream Vera Sans"]matplotlib.rcParams["font.family"] = "sans-serif"import seaborn as snssns.set(font_scale=1)sns.set_style("whitegrid", {'axes.grid' : False})sns.set_style("ticks")from matplotlib_venn import venn3,venn2from scipy import statsimport warningswarnings.filterwarnings("ignore")# indir = 'f3_coBinding_merge'indir = 'f4_cobinding_TFBS_venn'outdir = 'f5_atac_overlap_coBinding_TFBS'os.makedirs(outdir,exist_ok=True)atac_file = '../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed'alpha = .7selected_factors = {'MCF-7 top_TFBSCP':['FOXK2','ERG','RELA'],                    'MCF-7 top_zscored_TFBSCP':['FOXK2','ERG','RELA'],                    'HCT-116 top_TFBSCP':['ELF1','JUND','SRF',],                    'HCT-116 top_zscored_TFBSCP':['JUND','CEBPB','YY1']}for treat_flag in ['percentile_T','percentile_T_ExtendMerge'][:]:    for ct in ['MCF-7','HCT-116'][:]:        for factorType in ['top_TFBSCP','top_zscored_TFBSCP'][:]:            subdir = '{}_{}'.format(ct,factorType)            os.makedirs(outdir+os.sep+subdir,exist_ok=True)                        factors = selected_factors['{} {}'.format(ct,factorType)]                        prenames = factors + ['hg38_exons','hg38_introns','hg38_4k_promoter_geneID']                        outdf = pd.read_csv('{}/{}/{}_{}_cobinding.csv'.format(indir,subdir,treat_flag,ct,))                   # ==== bar plot for genomic annotations            dfs = [outdf,                   outdf[(outdf[prenames[0]]!=0)],                   outdf[(outdf[prenames[1]]!=0)],                   outdf[(outdf[prenames[2]]!=0)],                   outdf[(outdf[prenames[0]]!=0)&(outdf[prenames[1]]!=0)],                   outdf[(outdf[prenames[0]]!=0)&(outdf[prenames[1]]!=0)&(outdf[prenames[2]]!=0)]]            xticklabels = ['Union',                           '{}'.format('-'.join([i for i in prenames[:1]])),                           '{}'.format('-'.join([i for i in prenames[1:2]])),                           '{}'.format('-'.join([i for i in prenames[2:3]])),                           '{}'.format('-'.join([i for i in prenames[:2]])),                           '{}'.format('-'.join([i for i in prenames[:3]])),                           ]                        for ii in np.arange(len(xticklabels)):                outbed = '{}/{}/{}_{}_{}.bed'.format(outdir,subdir,treat_flag,ct,xticklabels[ii])                dfs[ii].to_csv(outbed,index=False,sep='\t',header=None)                overlapped_bed = '{}/{}/atac_overlapped_{}_{}_{}.bed'.format(outdir,subdir,treat_flag,ct,xticklabels[ii])                commandLine = 'bedtools intersect \\\n-a {} \\\n-b {} \\\n-wa -u > {}\n'.format(atac_file,outbed,overlapped_bed)                print(commandLine);os.system(commandLine)