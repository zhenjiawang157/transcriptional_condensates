bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/percentile_T_MCF-7_Union.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/atac_overlapped_percentile_T_MCF-7_Union.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/percentile_T_MCF-7_FOXK2.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/atac_overlapped_percentile_T_MCF-7_FOXK2.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/percentile_T_MCF-7_ERG.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/atac_overlapped_percentile_T_MCF-7_ERG.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/percentile_T_MCF-7_RELA.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/atac_overlapped_percentile_T_MCF-7_RELA.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/percentile_T_MCF-7_FOXK2-ERG.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/atac_overlapped_percentile_T_MCF-7_FOXK2-ERG.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/percentile_T_MCF-7_FOXK2-ERG-RELA.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/atac_overlapped_percentile_T_MCF-7_FOXK2-ERG-RELA.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/percentile_T_MCF-7_Union.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/atac_overlapped_percentile_T_MCF-7_Union.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/percentile_T_MCF-7_FOXK2.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/atac_overlapped_percentile_T_MCF-7_FOXK2.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/percentile_T_MCF-7_ERG.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/atac_overlapped_percentile_T_MCF-7_ERG.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/percentile_T_MCF-7_RELA.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/atac_overlapped_percentile_T_MCF-7_RELA.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/percentile_T_MCF-7_FOXK2-ERG.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/atac_overlapped_percentile_T_MCF-7_FOXK2-ERG.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/percentile_T_MCF-7_FOXK2-ERG-RELA.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/atac_overlapped_percentile_T_MCF-7_FOXK2-ERG-RELA.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/percentile_T_HCT-116_Union.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/atac_overlapped_percentile_T_HCT-116_Union.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/percentile_T_HCT-116_ELF1.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/atac_overlapped_percentile_T_HCT-116_ELF1.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/percentile_T_HCT-116_JUND.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/atac_overlapped_percentile_T_HCT-116_JUND.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/percentile_T_HCT-116_SRF.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/atac_overlapped_percentile_T_HCT-116_SRF.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/percentile_T_HCT-116_ELF1-JUND.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/atac_overlapped_percentile_T_HCT-116_ELF1-JUND.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/percentile_T_HCT-116_ELF1-JUND-SRF.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/atac_overlapped_percentile_T_HCT-116_ELF1-JUND-SRF.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/percentile_T_HCT-116_Union.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/atac_overlapped_percentile_T_HCT-116_Union.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/percentile_T_HCT-116_JUND.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/atac_overlapped_percentile_T_HCT-116_JUND.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/percentile_T_HCT-116_CEBPB.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/atac_overlapped_percentile_T_HCT-116_CEBPB.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/percentile_T_HCT-116_YY1.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/atac_overlapped_percentile_T_HCT-116_YY1.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/percentile_T_HCT-116_JUND-CEBPB.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/atac_overlapped_percentile_T_HCT-116_JUND-CEBPB.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/percentile_T_HCT-116_JUND-CEBPB-YY1.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/atac_overlapped_percentile_T_HCT-116_JUND-CEBPB-YY1.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/percentile_T_ExtendMerge_MCF-7_Union.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_MCF-7_Union.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/percentile_T_ExtendMerge_MCF-7_FOXK2.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_MCF-7_FOXK2.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/percentile_T_ExtendMerge_MCF-7_ERG.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_MCF-7_ERG.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/percentile_T_ExtendMerge_MCF-7_RELA.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_MCF-7_RELA.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/percentile_T_ExtendMerge_MCF-7_FOXK2-ERG.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_MCF-7_FOXK2-ERG.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/percentile_T_ExtendMerge_MCF-7_FOXK2-ERG-RELA.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_MCF-7_FOXK2-ERG-RELA.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/percentile_T_ExtendMerge_MCF-7_Union.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_MCF-7_Union.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/percentile_T_ExtendMerge_MCF-7_FOXK2.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_MCF-7_FOXK2.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/percentile_T_ExtendMerge_MCF-7_ERG.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_MCF-7_ERG.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/percentile_T_ExtendMerge_MCF-7_RELA.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_MCF-7_RELA.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/percentile_T_ExtendMerge_MCF-7_FOXK2-ERG.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_MCF-7_FOXK2-ERG.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/percentile_T_ExtendMerge_MCF-7_FOXK2-ERG-RELA.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/MCF-7_top_zscored_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_MCF-7_FOXK2-ERG-RELA.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/percentile_T_ExtendMerge_HCT-116_Union.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_HCT-116_Union.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/percentile_T_ExtendMerge_HCT-116_ELF1.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_HCT-116_ELF1.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/percentile_T_ExtendMerge_HCT-116_JUND.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_HCT-116_JUND.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/percentile_T_ExtendMerge_HCT-116_SRF.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_HCT-116_SRF.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/percentile_T_ExtendMerge_HCT-116_ELF1-JUND.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_HCT-116_ELF1-JUND.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/percentile_T_ExtendMerge_HCT-116_ELF1-JUND-SRF.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_HCT-116_ELF1-JUND-SRF.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/percentile_T_ExtendMerge_HCT-116_Union.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_HCT-116_Union.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/percentile_T_ExtendMerge_HCT-116_JUND.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_HCT-116_JUND.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/percentile_T_ExtendMerge_HCT-116_CEBPB.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_HCT-116_CEBPB.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/percentile_T_ExtendMerge_HCT-116_YY1.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_HCT-116_YY1.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/percentile_T_ExtendMerge_HCT-116_JUND-CEBPB.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_HCT-116_JUND-CEBPB.bed

bedtools intersect \
-a ../../../f9_TF_condensates_V3/data/TCGA//tcga_atac.bed \
-b f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/percentile_T_ExtendMerge_HCT-116_JUND-CEBPB-YY1.bed \
-wa -u > f5_atac_overlap_coBinding_TFBS/HCT-116_top_zscored_TFBSCP/atac_overlapped_percentile_T_ExtendMerge_HCT-116_JUND-CEBPB-YY1.bed

