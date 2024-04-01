class: Workflow
cwlVersion: v1.2

requirements: 
  ScatterFeatureRequirement: {}
  SubworkflowFeatureRequirement: {}

inputs:
  dataset_file: 
    type: File
  target_column:
    type: string
  k:
    type: int
  folds: 
    type: int[]

outputs:
  output_final:
    type: File
    outputSource: collect/output_final

steps:
  train_fold:
    run: train_fold.cwl
    scatter: current_fold
    in:
      dataset_file: dataset_file
      target_column: target_column
      k: k
      current_fold: folds
    out: [fold_results]
  collect:
    run: collect.cwl
    in:
      metrics: train_fold/fold_results
    out: [output_final]