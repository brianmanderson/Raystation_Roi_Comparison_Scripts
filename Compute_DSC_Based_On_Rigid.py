from connect import *

case = get_current("Case")
primary_exam = 'CT 3'
secondary_exam = 'CT 4'
roi_name = 'Liver_BMA_Program_4'
matrix = case.GetTotalTransformFromExaminations(FromExamination=primary_exam,ToExamination=secondary_exam)
dsc = case.SimilarityForRigidlyMappedRoiGeometry(FromImageName=primary_exam,ToImageName=secondary_exam,
                                                 RoiGeometryName=roi_name,RigidTransformation=matrix)
for i in dsc:
    print(i)