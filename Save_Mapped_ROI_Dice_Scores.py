from connect import *

patient = get_current("Patient")
case = get_current("Case")
MRN = patient.PatientID

rois_in_case = []
for name in case.PatientModel.RegionsOfInterest:
    print(name.Name)
    rois_in_case.append(name.Name)
registration_value = None
for Registration in case.Registrations:
    for structure_reg in Registration.StructureRegistrations:
        if structure_reg.Name == 'ANACONDA with MI1':
            registration_value = structure_reg
            break
    if registration_value:
        break
if registration_value:
    fid = open('\\\\mymdafiles\\di_data1\\Morfeus\\MMMcCulloch\\dice_comparison_' + str(MRN) + '.txt', 'w+')
    fid.write(MRN + '\n')
    fid.write('ROI' + ',' + 'Dice' + ',' + 'Average_DTA' + ',' + 'Max_DTA' + ',' + 'Min_DTA\n')
    for roi in rois_in_case:
        if roi == 'External':
            continue
        try:
            dict_val = registration_value.SimilarityForDeformablyMappedRoiGeometry(RoiGeometryName=roi)
            dict_val_surface = registration_value.RoiSurfaceToSurfaceDistanceForDeformablyMappedRoiGeometry(RoiGeometryName=roi)
            print(roi)
            print(dict_val.DiceSimilarityCoefficient)
            fid.write(str(roi) + ',' + str(dict_val.DiceSimilarityCoefficient) + ',' + str(dict_val_surface['Average']) +',' + str(dict_val_surface['Max']) + ',' + str(dict_val_surface['Min']) + '\n')
        except:
            continue
    fid.close()