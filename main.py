from sicumon.sicum import Sicum
from sicumon.db import Db
import io

print(Db.generate_file_url('files/yom_hamea.pdf'))


"""bin=open('yom_hamea.pdf','rb').read()
f = io.BytesIO(bin)

meta = Sicum.from_dict(
    {
        'fileName': 'yom_hamea.pdf',
        'subject': 'Other',
        'uploaderName': 'Yonatan2'
    }
)

Db.new_file(file=f, file_meta=meta)"""