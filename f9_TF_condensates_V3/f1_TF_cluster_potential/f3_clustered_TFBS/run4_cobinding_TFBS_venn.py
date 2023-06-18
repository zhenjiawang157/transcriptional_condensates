import sys,argparseimport os,glob,reimport numpy as npimport pandas as pd#from GenomeData import *import matplotlib# matplotlib.use('Agg')import matplotlib.pyplot as pltmatplotlib.rcParams['font.size']=13matplotlib.rcParams["font.sans-serif"] = ["Arial", "Liberation Sans", "Bitstream Vera Sans"]matplotlib.rcParams["font.family"] = "sans-serif"import seaborn as snssns.set(font_scale=1)sns.set_style("whitegrid", {'axes.grid' : False})sns.set_style("ticks")from matplotlib_venn import venn3,venn2from scipy import statsimport warningswarnings.filterwarnings("ignore")indir = 'f3_coBinding_merge'outdir = 'f4_cobinding_TFBS_venn'os.makedirs(outdir,exist_ok=True)alpha = .7selected_factors = {'MCF-7 top_TFBSCP':['NR2F2','MAX','ERG'],                    'MCF-7 top_zscored_TFBSCP':['ERG','E2F1','MYC'],                    'HCT-116 top_TFBSCP':['JUND','CEBPB','MAX'],                    'HCT-116 top_zscored_TFBSCP':['SRF','JUND','CEBPB']}for treat_flag in ['percentile_T','percentile_T_ExtendMerge'][:]:    for ct in ['MCF-7','HCT-116'][:]:        for factorType in ['top_TFBSCP','top_zscored_TFBSCP'][:]:            subdir = '{}_{}'.format(ct,factorType)            os.makedirs(outdir+os.sep+subdir,exist_ok=True)                        factors = selected_factors['{} {}'.format(ct,factorType)]                        prenames = factors + ['hg38_exons','hg38_introns','hg38_4k_promoter_geneID']            outdf = pd.DataFrame()            for prename in prenames[:]:                infile = '{}/{}/{}.merge.{}.overlapped.bed'.format(indir,subdir,treat_flag,prename)                df = pd.read_csv(infile,header=None,sep='\t')                df.columns = ['chr','start','end',prename]                if outdf.shape[0]==0:                    outdf = pd.concat([outdf,df],axis=1)                else:                    outdf = pd.concat([outdf,df[prename]],axis=1)            outdf.loc[outdf['hg38_introns']!=0,'annotation']='Intron'            outdf.loc[outdf['hg38_exons']!=0,'annotation']='Exon'            outdf.loc[outdf['hg38_4k_promoter_geneID']!=0,'annotation']='Promoter'            outdf['annotation'] = outdf['annotation'].fillna('Distal')                # ==== save the overlap infor                outdf.to_csv('{}/{}/{}_{}_cobinding.csv'.format(outdir,subdir,treat_flag,ct,),index=False)                                    # ==== venn for co-binding            a = set(outdf[outdf[factors[0]]!=0].index)            b = set(outdf[outdf[factors[1]]!=0].index)            c = set(outdf[outdf[factors[2]]!=0].index)            # total=2723010            # s,p = stats.fisher_exact([[len(a.intersection(b)),len(a)],[len(b),total-len(b)]])            # print(celltype,s,p)            set_labels = factors            colors = ['tab:red','tab:blue','tab:green']            colors = ['salmon','steelblue','mediumaquamarine']            plt.figure(figsize=(2.5,2.5))            out = venn3([a,b,c],set_labels=set_labels,set_colors=colors, alpha=alpha)            for text in out.set_labels:                text.set_fontsize(11)            for text in out.subset_labels:                text.set_fontsize(8)            plt.title(ct,fontsize=12)            plt.savefig('{}/{}/{}_{}_venn.pdf'.format(outdir,subdir,treat_flag,ct),bbox_inches = 'tight',pad_inches=0.1,transparent=True)            plt.show()            plt.close()                        # continue                                # ==== bar plot for genomic annotations            info_df = pd.DataFrame()            plt.figure(figsize=(3,3))            dfs = [outdf,                   outdf[(outdf[prenames[0]]!=0)],                   outdf[(outdf[prenames[1]]!=0)],                   outdf[(outdf[prenames[2]]!=0)],                   outdf[(outdf[prenames[0]]!=0)&(outdf[prenames[1]]!=0)],                   outdf[(outdf[prenames[0]]!=0)&(outdf[prenames[1]]!=0)&(outdf[prenames[2]]!=0)]]            xticklabels = ['All',                           '{}'.format('-'.join([i for i in prenames[:1]])),                           '{}'.format('-'.join([i for i in prenames[1:2]])),                           '{}'.format('-'.join([i for i in prenames[2:3]])),                           '{}'.format('-'.join([i for i in prenames[:2]])),                           '{}'.format('-'.join([i for i in prenames[:3]])),                           ]            colors = ['tab:green','tab:blue','tab:gray','tab:orange'][::-1]            colors = ['mediumaquamarine','steelblue','silver','salmon'][::-1]            labels = ["Promoter","Exon","Intron","Distal"][::-1]            positions = np.arange(len(dfs))            for position in positions:                a = (dfs[position]['annotation']==labels[0]).sum()                b = (dfs[position]['annotation']==labels[1]).sum()                c = (dfs[position]['annotation']==labels[2]).sum()                d = (dfs[position]['annotation']==labels[3]).sum()                # e = (dfs[position]['{}_SE'.format(celltype)]!=0).sum()                # e = ((dfs[position]['annotation']==labels[0])&(dfs[position]['{}_SE'.format(celltype)]!=0)).sum()                total = a+b+c+d                info_df.loc[xticklabels[position],labels[0]]=a                info_df.loc[xticklabels[position],labels[1]]=b                info_df.loc[xticklabels[position],labels[2]]=c                info_df.loc[xticklabels[position],labels[3]]=d                info_df.loc[xticklabels[position],'total']=total                # info_df.loc[xticklabels[position],'SE overlapped']=e                # info_df.loc[xticklabels[position],'%SE overlapped']=np.round(e/total,3)                g0 = plt.bar(position, 100*a/total, bottom=0, width=.68, lw=0, color=colors[0],label=labels[0],alpha=alpha)                g1 = plt.bar(position, 100*b/total, bottom=100*a/total, width=.68, lw=0, color=colors[1],label=labels[1],alpha=alpha)                g2 = plt.bar(position, 100*c/total, bottom=100*(a+b)/total, width=.68, lw=0, color=colors[2],label=labels[2],alpha=alpha)                g3 = plt.bar(position, 100*d/total, bottom=100*(a+b+c)/total, width=.68, lw=0, color=colors[3],label=labels[3],alpha=alpha)                plt.text(position,0, a,va='bottom',ha='center',fontsize=9)                plt.text(position,100*a/total, b,va='bottom',ha='center',fontsize=9)                plt.text(position,100*(a+b)/total, c,va='bottom',ha='center',fontsize=9)                plt.text(position,100*(a+b+c)/total, d,va='bottom',ha='center',fontsize=9)                position+=1            info_df.to_csv('{}/{}/{}_{}_annotation.csv'.format(outdir,subdir,treat_flag,ct))            plt.ylabel('TFBS co-binding (%)',fontsize=13)            plt.ylim([0,100])            plt.legend([g3,g2,g1,g0],["Promoter","Exon","Intron","Intergenic"],                       loc=1,bbox_to_anchor=(1.5,1.05),fontsize=13,                       borderaxespad=0.2,labelspacing=.2,handletextpad=0.2,handlelength=1,frameon=False)            plt.axes().set_xticks(positions)             sns.despine(offset=0, trim=True)            plt.axes().spines['bottom'].set_visible(False)            plt.axes().set_xticklabels(xticklabels,rotation=45,ha='right',fontsize=13)             plt.axes().tick_params(axis='x',direction='out', length=0, width=.8, colors='black')            plt.title(ct,fontsize=12)            plt.savefig('{}/{}/{}_{}_annotation.pdf'.format(outdir,subdir,treat_flag,ct),bbox_inches = 'tight',pad_inches=0.1,transparent=True)            plt.show()            plt.close()                                        # ==== bar plot of SE overlap             # plt.figure(figsize=(3,3))            # positions = np.arange(len(dfs))            # for position in positions:            #     val = info_df.loc[xticklabels[position],'%SE overlapped']            #     val_num = info_df.loc[xticklabels[position],'SE overlapped']            #     g = plt.bar(position, val, width=.68, lw=0, color='tab:red',alpha=alpha)            #     plt.text(position,val, int(val_num),va='bottom',ha='center',fontsize=9)            #     position+=1            # plt.ylabel('SE overlapped (%)',fontsize=13)            # # plt.ylim([0,.15])            # plt.axes().set_xticks(positions)             # sns.despine(offset=0, trim=True)            # plt.axes().spines['bottom'].set_visible(False)            # plt.axes().set_xticklabels(xticklabels,rotation=45,ha='right',fontsize=13)             # plt.axes().tick_params(axis='x',direction='out', length=0, width=.8, colors='black')            # plt.title(celltype,fontsize=12)            # plt.savefig('{}/{}_SE_overlapped.pdf'.format(outdir,celltype),bbox_inches = 'tight',pad_inches=0.1,transparent=True)            # plt.show()            # plt.close()            