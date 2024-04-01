cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python", "/app/train_fold.py"]

hints:
  DockerRequirement:
    dockerPull: sonjagalovic/racunarstvo-u-oblaku:assignment4

inputs:
  dataset_file:
    type: File
    inputBinding:
      position: 1
  target_column:
    type: string
    inputBinding:
      position: 2
  k:
    type: int
    inputBinding:
      position: 3
  current_fold:
    type: int
    inputBinding:
      position: 4

stdout: output.txt

outputs:
  fold_results:
    type: string
    outputBinding:
      glob: output.txt
      loadContents: true
      outputEval: $(self[0].contents)