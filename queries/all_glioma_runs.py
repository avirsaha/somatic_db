# Description:
# Pull out all glioma samples in SVD
#
# Date: 23/03/23 - NT
# Use: python manage.py shell < /home/ew/somatic_db/queries/all_glioma_runs.py (with somatic_variant_db env activated)

from analysis.models import SampleAnalysis, Panel

# Headers and liat to save output
outlist = [['run']]

# Get all samples in glioma dna panel
glioma_panel_dna = Panel.objects.get(panel_name = 'Glioma', dna_or_rna = 'DNA')
glioma_samples_dna = SampleAnalysis.objects.filter(panel = glioma_panel_dna)

# Loop through samples to get panel, sample and run
for s in glioma_samples_dna:
	outlist.append([str(s.worksheet.run)])

# Get all samples in glioma rna panel
glioma_panel_rna = Panel.objects.get(panel_name = 'Glioma', dna_or_rna = 'RNA')
glioma_samples_rna = SampleAnalysis.objects.filter(panel = glioma_panel_rna)

# Loop through samples to get panel, sample and run
for s in glioma_samples_rna:
        outlist.append([str(s.worksheet.run)])

# Output data to screen 
for line in outlist:
	print(','.join(line))
