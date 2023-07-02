from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import String, Integer, Enum
from sqlalchemy.orm import relationship
from Database import Base


class ProvinsiInfo(Base):
    __tablename__ = "provinsi"
    nama_provinsi = Column("nama_provinsi", String, primary_key=True, index=True)
    kabupaten = relationship("KabupatenInfo", back_populates="provinsi")

class KabupatenInfo(Base):
    __tablename__ = "kabupaten"
    nama_kabupaten = Column("nama_kabupaten", String, primary_key=True, index=True)
    nama_provinsi = Column("nama_provinsi", String, ForeignKey('provinsi.nama_provinsi'))
    provinsi = relationship("ProvinsiInfo", back_populates="kabupaten")
    kecamatan = relationship("KecamatanInfo", back_populates="kabupaten")

class KecamatanInfo(Base):
    __tablename__ = "kecamatan"
    nama_kecamatan = Column(String, primary_key=True, index=True)
    nama_kabupaten = Column("nama_kabupaten", String, ForeignKey('kabupaten.nama_kabupaten'))
    kabupaten = relationship("KabupatenInfo", back_populates="kecamatan")

#     kabupaten = relationship("kabupaten")