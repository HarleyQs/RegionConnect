from pydantic import BaseModel
from typing import Optional, List


#========================PROVINSI======================#

class CreateAndUpdateProvinsi(BaseModel):
    nama_provinsi: str


class Provinsi(CreateAndUpdateProvinsi):
    nama_provinsi: str

    class Config:
        orm_mode = True


class PaginatedProvinsiInfo(BaseModel):
    limit: int
    offset: int
    data: List[Provinsi]

#======================KABUPATEN======================#


class CreateAndUpdateKabupaten(BaseModel):
    nama_kabupaten: str
    nama_provinsi: Optional[str]


class Kabupaten(CreateAndUpdateKabupaten):
    nama_kabupaten: str

    class Config:
        orm_mode = True


class PaginatedKabupatenInfo(BaseModel):
    limit: int
    offset: int
    data: List[Kabupaten]

#======================KECAMATAN======================#
#
class CreateAndUpdateKecamatan(BaseModel):
    nama_kecamatan: str
    nama_kabupaten: Optional[str]

class Kecamatan(CreateAndUpdateKecamatan):
    nama_kecamatan: str

    class Config:
        orm_mode = True

class PaginatedKecamatanInfo(BaseModel):
    limit: int
    offset: int
    data: List[Kecamatan]
