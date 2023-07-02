class ProvinsiInfoException(Exception):
    ...


class ProvinsiInfoNotFoundError(ProvinsiInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Provinsi Not Found"


class ProvinsiInfoAlreadyExistError(ProvinsiInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Provinsi Info Already Exist"

class ProvinsiContainsKabupatenError(ProvinsiInfoException):
    def __init__(self):
        self.status_code = 400
        self.detail = "Provinsi Contains Kabupaten"


class KabupatenInfoException(Exception):
    ...


class KabupatenInfoNotFoundError(KabupatenInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Kabupaten Not Found"


class KabupatenInfoAlreadyExistError(KabupatenInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Kabupaten Info Already Exist"

class KabupatenContainsKecamatanError(ProvinsiInfoException):
    def __init__(self):
        self.status_code = 401
        self.detail = "Kabupaten Contains Kecamatan"


class KecamatanInfoException(Exception):
    ...


class KecamatanInfoNotFoundError(KecamatanInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Kabupaten Not Found"


class KecamatanInfoAlreadyExistError(KecamatanInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Kabupaten Info Already Exist"

