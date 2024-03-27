class: Workflow
cwlVersion: v1.0

inputs:
  app_preprocess: File
  app_train: File
  dataset_file: File
  target_column:
    type: string
  training_percentage:
    type: float

outputs:
  performance_metrics:
    type: File
    outputSource: train_and_evaluate/performance_metrics

steps:
  preprocess:
    run: preprocessing.cwl
    in:
      app_preprocess: app_preprocess
      dataset_file: dataset_file
    out: [cleaned_dataset]

  train_and_evaluate:
    run: train_and_evaluate.cwl
    in:
      app_train: app_train
      cleaned_dataset: preprocess/cleaned_dataset
      target_column: target_column
      training_percentage: training_percentage
    out: [performance_metrics]