from connect import *
import os

out_path = r'\\d1prpccifs\radphys_pt_care\court-lab\CAOwens\Raystation_Measurements'
case = get_current("Case")
exam = get_current("Examination")
patient = get_current("Patient")

roi_pairs = [['RoiA','RoiB'],
             ['RoiA2','RoiB2']] # Write in your pairs of ROIs to compare
data_out = {}
metrics = ['DiceSimilarityCoefficient','MeanDistanceToAgreement','MaxDistanceToAgreement']
for rois in roi_pairs:
    roi_a = rois[0]
    roi_b = rois[1]
    dict_val = case.PatientModel.StructureSets[exam.Name].ComparisonOfRoiGeometries(RoiA=roi_a,RoiB=roi_b,ComputeDistanceToAgreementMeasures=True)
    data_out[roi_a] = {}
    for metric in metrics:
        data_out[roi_a][metric] = str(dict_val[metric])

out_path = os.path.join(out_path,patient.PatientID)
if not os.path.exists(out_path):
    os.makedirs(out_path)
fid = open(os.path.join(out_path,'Results.txt'),'w+')
fid.write('ROI_Name,')
for metric in metrics:
    fid.write(metric+',')
fid.write('\n')
for roi in data_out:
    fid.write(roi+',')
    for metric in data_out[roi]:
        fid.write(data_out[roi][metric] + ',')
    fid.write('\n')
fid.close()
