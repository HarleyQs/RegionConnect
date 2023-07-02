from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from Database import get_db
from exception import ProvinsiInfoException, KabupatenInfoException, KecamatanInfoException
from Schemas import Provinsi, CreateAndUpdateProvinsi, PaginatedProvinsiInfo, Kecamatan, Kabupaten, PaginatedKecamatanInfo, CreateAndUpdateKecamatan, CreateAndUpdateKabupaten, PaginatedKabupatenInfo

from crud import (get_all_provinsi, 
                  get_provinsi_info_by_name, 
                  create_provinsi_info, 
                  update_provinsi_info, 
                  delete_provinsi_info, 
                  get_kabupaten_by_name, 
                  get_all_kabupaten,
                  get_all_kabupaten_by_provinsi,
                  create_kabupaten_info,
                  update_kabupaten_info,
                  delete_kabupaten_info,
                  get_all_kecamatan,
                  get_all_kecamatan_by_kabupaten,
                  get_kecamatan_by_name,
                  update_kecamatan_info,
                  delete_kecamatan_info,
                  create_kecamatan_info)


router = APIRouter()

@cbv(router)
class ProvinsiRouter:
    sessions: Session = Depends(get_db)

    @router.get("/provinsi", response_model=PaginatedProvinsiInfo)
    async def list_provinsi(self, limit: int = 10, offset: int = 0):

        provinsi_list = await get_all_provinsi(self.sessions, limit, offset)
        response = {"limit": limit, "offset": offset, "data": provinsi_list}
    
        return response

    @router.post("/provinsi")
    async def add_provinsi(self, provinsi_info: CreateAndUpdateProvinsi):
        try:
            provinsi_info = create_provinsi_info(self.sessions, provinsi_info)
            return provinsi_info
        except ProvinsiInfoException as cie:
            raise HTTPException(**cie.__dict__)
        
    @router.get("/kabupaten/{nama_provinsi}")
    async def list_kabupaten_by_provinsi(self, nama_provinsi:str):
        kabupaten_list = get_all_kabupaten_by_provinsi(self.sessions, nama_provinsi)
        
        response = {"data": kabupaten_list}
        
        return response

    @router.get("/kabupaten", response_model=PaginatedKabupatenInfo)
    async def list_kabupaten(self, limit: int = 10, offset: int = 0):
        kabupaten_list = get_all_kabupaten(self.sessions, limit, offset)
        response = {"limit":limit, "offset": offset, "data": kabupaten_list}
        
        return response

    @router.post("/kabupaten")
    async def add_kabupaten(self, kabupaten_info: CreateAndUpdateKabupaten):
        try:
            kabupaten_info = create_kabupaten_info(self.sessions, kabupaten_info)
            return kabupaten_info
        except KabupatenInfoException as cie:
            raise HTTPException(**cie.__dict__)
    
    @router.get("/kecamatan/{nama_kabupaten}")
    async def list_kecamatan_by_kabupaten(self, nama_kabupaten: str):
        kecamatan_list = get_all_kecamatan_by_kabupaten(self.sessions, nama_kabupaten)
        response = {"data": kecamatan_list}
        return response
    
    @router.get("/kecamatan", response_model=PaginatedKecamatanInfo)
    async def list_kecamatan(self, limit: int=10, offset: int= 0):
        kecamatan_list = get_all_kecamatan(self.sessions, limit, offset)
        response = {"limit": limit, "offset": offset, "data": kecamatan_list}
        
        return response
    
    @router.post("/kecamatan")
    async def add_kecamatan(self, kecamatan_info: CreateAndUpdateKecamatan):
        try:
            kecamatan_info = create_kecamatan_info(self.sessions, kecamatan_info)
            return kecamatan_info
        except KecamatanInfoException as cie:
            raise HTTPException(**cie.__dict__)





@router.get("/provinsi/{nama_provinsi}", response_model=Provinsi)
async def get_provinsi_info(nama_provinsi: str, session: Session = Depends(get_db)):
    try:
        provinsi_info = get_provinsi_info_by_name(session, nama_provinsi)
        return provinsi_info
    except ProvinsiInfoException as cie:
        raise HTTPException(**cie.__dict__)


@router.put("/provinsi/{nama_provinsi}")
async def update_provinsi(nama_provinsi: str, new_info: CreateAndUpdateProvinsi, session: Session = Depends(get_db)):
    try:
        provinsi_info = update_provinsi_info(session, nama_provinsi, new_info)
        return provinsi_info
    except ProvinsiInfoException as cie:
        raise HTTPException(**cie.__dict__)

@router.delete("/provinsi/{nama_provinsi}")
async def delete_provinsi(nama_provinsi: str, session: Session = Depends(get_db)):
    try:
        return delete_provinsi_info(session, nama_provinsi)
    except ProvinsiInfoException as cie:
        raise HTTPException(**cie.__dict__)




@router.get("/kabupaten/{nama_kabupaten}", response_model=Kabupaten)
async def get_kabupaten_info_by_name(nama_kabupaten: str, session: Session = Depends(get_db)):
    try:
        kabupaten_info = get_kabupaten_by_name(session, nama_kabupaten)
        return kabupaten_info
    except KabupatenInfoException as cie:
        raise HTTPException(**cie.__dict__)


@router.put("/kabupaten/{nama_kabupaten}", response_model=Kabupaten)
async def update_kabupaten(nama_kabupaten: str, new_info: CreateAndUpdateKabupaten, session: Session = Depends(get_db)):
    try:
        kabupaten_info = update_kabupaten_info(session, nama_kabupaten, new_info)
        return kabupaten_info
    except KabupatenInfoException as cie:
        raise HTTPException(**cie.__dict__)

@router.delete("/kabupaten/{nama_kabupaten}")
async def delete_kabupaten(nama_kabupaten: str, session: Session = Depends(get_db)):
    try:
        return await delete_kabupaten_info(session, nama_kabupaten)
    except KabupatenInfoException as cie:
        raise HTTPException(status_code=cie.status_code, detail=cie.detail)
    


@router.get("/kecamatan/{nama_kecamatan}", response_model=Kecamatan)
async def get_kecamatan_info_by_name( nama_kecamatan: str, session: Session = Depends(get_db)):
    try:
        kecamatan_info = get_kecamatan_info_by_name(session, nama_kecamatan)
        return kecamatan_info
    except KecamatanInfoException as cie:
        raise HTTPException(**cie.__dict__)


@router.put("/kecamatan/{nama_kecamatan}", response_model=Kecamatan)
async def update_kecamatan( nama_kecamatan: str, new_info: CreateAndUpdateKecamatan, session: Session = Depends(get_db)):
    try:
        kecamatan_info = update_kecamatan_info(session,nama_kecamatan, new_info)
        return kecamatan_info
    except KecamatanInfoException as cie:
        raise HTTPException(**cie.__dict__)

@router.delete("/kecamatan/{nama_kecamatan}")
async def delete_kecamatan( nama_kecamatan: str, session: Session = Depends(get_db)):
    try:
        return delete_kecamatan_info(session, nama_kecamatan)
    except KecamatanInfoException as cie:
        raise HTTPException(**cie.__dict__)
