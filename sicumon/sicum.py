class Sicum:
    fileName: str
    fileKey: str
    subject: str
    uploadDate: int
    uploaderName: str


    def __init__(self, fileName: str, subject: str, uploaderName: str, fileKey: str = None, uploadDate: int = None):
        self.fileName = fileName
        self.fileKey = fileKey
        self.subject = subject
        self.uploadDate = uploadDate
        self.uploaderName = uploaderName
    
    def from_dict(data: dict):
        return Sicum(fileName=data.get('fileName'), fileKey=data.get('fileKey'), subject=data.get('subject'), uploadDate=data.get('uploadDate'), uploaderName=data.get('uploaderName'))
