class: CommandLineTool
cwlVersion: v1.0
baseCommand: ["python"]

hints:
  DockerRequirement:
    dockerPull: sonjagalovic/racunarstvo-u-oblaku:assignment3
inputs:
  app_train:
    type: File
    inputBinding:
      position: 1
  cleaned_dataset:
    type: File
    inputBinding:
      position: 2
  target_column:
    type: string
    inputBinding:
      position: 3
  training_percentage:
    type: float
    inputBinding:
      position: 4

outputs:
  performance_metrics:
    type: stdout
stdout: performance_metrics.txt