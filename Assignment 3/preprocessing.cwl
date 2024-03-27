cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python"]

hints:
  DockerRequirement:
    dockerPull: sonjagalovic/racunarstvo-u-oblaku:assignment3

inputs:
  app_preprocess:
    type: File
    inputBinding:
      position: 1
  dataset_file:
    type: File
    inputBinding:
      position: 2

outputs:
  cleaned_dataset:
    type: stdout
stdout: cleaned_dataset.csv