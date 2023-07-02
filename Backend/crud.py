from typing import List
from sqlalchemy.orm import Session
from model import ProvinsiInfo, KabupatenInfo, KecamatanInfo
from Schemas import CreateAndUpdateProvinsi, CreateAndUpdateKabupaten, CreateAndUpdateKecamatan
from exception import (ProvinsiInfoAlreadyExistError,
                        ProvinsiInfoNotFoundError,
                        KabupatenInfoNotFoundError,
                        KabupatenInfoAlreadyExistError,
                        KabupatenContainsKecamatanError,
                        KecamatanInfoAlreadyExistError,
                        ProvinsiContainsKabupatenError,
                        KecamatanInfoNotFoundError)

# =========================Provinsi==========================
async def get_all_provinsi(session: Session, limit: int, offset: int) -> List[ProvinsiInfo]:
    return session.query(ProvinsiInfo).offset(offset).limit(limit).all()


def get_provinsi_info_by_name(session: Session, provinsi_id: str) -> ProvinsiInfo:
    provinsi_info = session.query(ProvinsiInfo).get(provinsi_id)

    if provinsi_info is None:
        raise ProvinsiInfoNotFoundError

    return provinsi_info


def create_provinsi_info(session: Session, provinsi_info: CreateAndUpdateProvinsi) -> ProvinsiInfo:
    provinsi_details = session.query(ProvinsiInfo).filter(ProvinsiInfo.nama_provinsi == provinsi_info.nama_provinsi).first()

    if provinsi_details is not None:
        raise ProvinsiInfoAlreadyExistError

    new_provinsi_info = ProvinsiInfo(**provinsi_info.dict())
    session.add(new_provinsi_info)
    session.commit()
    session.refresh(new_provinsi_info)
    return new_provinsi_info


def update_provinsi_info(session: Session, _name: str, info_update: CreateAndUpdateProvinsi) -> ProvinsiInfo:
    provinsi_info = get_provinsi_info_by_name(session, _name)
    if provinsi_info is  None:
        raise ProvinsiInfoNotFoundError

    provinsi_info.nama_provinsi = info_update.nama_provinsi

    session.commit()
    session.refresh(provinsi_info)

    return provinsi_info


def delete_provinsi_info(session: Session, _name: str):
    provinsi_info = get_provinsi_info_by_name(session, _name)

    if provinsi_info is None:
        raise ProvinsiInfoNotFoundError
    if get_all_kabupaten_by_provinsi(session, nama_provinsi= _name):
        raise ProvinsiContainsKabupatenError
    session.delete(provinsi_info)
    session.commit()

    return

# =========================Kabupaten==========================


def get_all_kabupaten(session: Session, limit: int, offset: int)->List[KabupatenInfo]:
    return session.query(KabupatenInfo).offset(offset).limit(limit).all()

def get_all_kabupaten_by_provinsi(session: Session, nama_provinsi: str)->List[KabupatenInfo]:
    provinsi_info = get_provinsi_info_by_name(session, nama_provinsi)
    if provinsi_info is None:
        raise ProvinsiInfoNotFoundError
    return session.query(KabupatenInfo).filter_by(nama_provinsi=nama_provinsi).all()

def get_kabupaten_by_name(session: Session, nama_kabupaten: str):
    kabupaten_info = session.query(KabupatenInfo).get(nama_kabupaten)

    if kabupaten_info is None:
        raise KabupatenInfoNotFoundError
    return kabupaten_info



def create_kabupaten_info(session:Session, kabupaten_info=CreateAndUpdateKabupaten) -> KabupatenInfo:
    provinsi_details = get_provinsi_info_by_name(session, kabupaten_info.nama_provinsi)
    if provinsi_details is None:
        raise ProvinsiInfoNotFoundError

    kabupaten_details = session.query(KabupatenInfo).filter(KabupatenInfo.nama_kabupaten == kabupaten_info.nama_kabupaten).first()

    if kabupaten_details is not None:
        raise KabupatenInfoAlreadyExistError

    new_kabupaten_info = KabupatenInfo(**kabupaten_info.dict())
    session.add(new_kabupaten_info)
    session.commit()
    session.refresh(new_kabupaten_info)
    return new_kabupaten_info

def update_kabupaten_info(session: Session, nama_kabupaten: str, info_update: CreateAndUpdateKabupaten) -> KabupatenInfo:
    kabupaten_info = get_kabupaten_by_name(session, nama_kabupaten)

    if kabupaten_info is None:
        raise KabupatenInfoNotFoundError

    kabupaten_info.nama_kabupaten = info_update.nama_kabupaten
    kabupaten_info.nama_provinsi = info_update.nama_provinsi

    session.commit()
    session.refresh(kabupaten_info)

    return kabupaten_info


async def delete_kabupaten_info(session: Session, nama_kabupaten: str):
    kabupaten_info = get_kabupaten_by_name(session, nama_kabupaten)

    if kabupaten_info is None:
        raise KabupatenInfoNotFoundError
    kecamatan_info = get_all_kecamatan_by_kabupaten(session, nama_kabupaten)
    if  kecamatan_info:
        raise KabupatenContainsKecamatanError
    session.delete(kabupaten_info)
    session.commit()
    return "SUCCSES"

# ========================KECAMATAN============================


def get_all_kecamatan(session: Session, limit: int, offset: int)->List[KecamatanInfo]:
    return session.query(KecamatanInfo).offset(offset).limit(limit).all()

def get_all_kecamatan_by_kabupaten(session: Session, nama_kabupaten: str)->List[KecamatanInfo]:
    kabupaten_info = get_kabupaten_by_name(session, nama_kabupaten)
    if kabupaten_info is None:
        raise KabupatenInfoNotFoundError
    return session.query(KecamatanInfo).filter_by(nama_kabupaten=nama_kabupaten).all()

def get_kecamatan_by_name(session: Session, nama_kecamatan: str):
    kecamatan_info = session.query(KecamatanInfo).get(nama_kecamatan)

    if kecamatan_info is None:
        raise KecamatanInfoNotFoundError
    return kecamatan_info



def create_kecamatan_info(session:Session, kecamatan_info=CreateAndUpdateKecamatan) -> KecamatanInfo:
    kabupaten_details = get_kabupaten_by_name(session, kecamatan_info.nama_kabupaten)
    if kabupaten_details is None:
        raise KabupatenInfoNotFoundError

    kecamatan_details = session.query(KecamatanInfo).filter(KecamatanInfo.nama_kecamatan == kecamatan_info.nama_kecamatan).first()

    if kecamatan_details is not None:
        raise KecamatanInfoAlreadyExistError

    new_kecamatan_info = KecamatanInfo(**kecamatan_info.dict())
    session.add(new_kecamatan_info)
    session.commit()
    session.refresh(new_kecamatan_info)
    return new_kecamatan_info

def update_kecamatan_info(session: Session, nama_kecamatan: str, info_update: CreateAndUpdateKecamatan) -> KecamatanInfo:
    kecamatan_info = get_kecamatan_by_name(session, nama_kecamatan)

    if kecamatan_info is None:
        raise KecamatanInfoNotFoundError

    kecamatan_info.nama_kabupaten = info_update.nama_kabupaten
    kecamatan_info.nama_kecamatan = info_update.nama_kecamatan

    session.commit()
    session.refresh(kecamatan_info)

    return kecamatan_info


def delete_kecamatan_info(session: Session, nama_kecamatan: str):
    kecamatan_info = get_kecamatan_by_name(session, nama_kecamatan)

    if kecamatan_info is None:
        raise KecamatanInfoNotFoundError
    session.delete(kecamatan_info)
    session.commit()

    return "SUCCSES"