class: Workflow
cwlVersion: v1.2

inputs:
  dataset_file: File
  target_column:
    type: string
  training_percentage:
    type: float

outputs:
  performance_metrics:
    type: File
    outputSource: training/performance_metrics

steps:
  preprocess:
    run: preprocessing.cwl
    in:
      dataset_file: dataset_file
    out: [cleaned_dataset]

  training:
    run: training.cwl
    in:
      cleaned_dataset: preprocess/cleaned_dataset
      target_column: target_column
      training_percentage: training_percentage
    out: [performance_metrics]