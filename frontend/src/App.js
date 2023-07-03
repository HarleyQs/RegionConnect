import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import pic from "./RegionConnectLogo.png";
import 'bootstrap/dist/css/bootstrap.min.css';
import { useMediaQuery } from 'react-responsive';
import ProvinsiView from './components/Provinsi/ProvinsiListView';
import KabupatenView from './components/Kabupaten/KabupatenListView';
import KecamatanView from './components/Kecamatan/KecamatanListView';



const apiUrl = `https://bbd1-180-252-125-38.ngrok-free.app`
function App() {
  // axios.get(apiUrl,  {headers: {'ngrok-skip-browser-warning': 'true'}}).then((res) => console.log(res))
  const isMobile = useMediaQuery({ maxWidth: 950});

  const [provinsiList, setProvinsiList] = useState([]);
  const [kabupatenList, setKabupatenList] = useState([]);
  const [kecamatanList, setKecamatanList] = useState([]);

  const [provinsi, setProvinsi] = useState('');
  const [kabupaten, setKabupaten] = useState('');
  const [kecamatan, setKecamatan] = useState('');

  // Read all provinsi
  
  useEffect(() => {
    axios.get(apiUrl+'/provinsi',  {headers: {'ngrok-skip-browser-warning': 'true'}}).then((res) => {
      console.log(res.data);
      setProvinsiList(res.data.data);
    });
  }, []);

  // Read all kabupaten
  useEffect(() => {
    axios.get(apiUrl +'/kabupaten', {headers: {'ngrok-skip-browser-warning': 'true'}}).then((res) => {
      console.log(res.data);
      setKabupatenList(res.data.data);
    });
  }, []);

  // Read all kecamatan
  useEffect(() => {
    axios.get(apiUrl + '/kecamatan', {headers: {'ngrok-skip-browser-warning': 'true'}}).then((res) => {
      console.log(res.data);
      setKecamatanList(res.data.data);
    });
  }, []);

  // add provinsi
  const addProvinsiHandler = () => {
    if (provinsi.trim() === '') {
      // Display a warning message to the user
      alert('Nama provinsi tidak boleh kosong.');
      return;
    }
    axios
      .post(apiUrl+'/provinsi', { nama_provinsi: provinsi })
      .then((res) => {
        console.log(res);
        window.location.reload();
      })
      .catch((error) => {
        if (error.response && error.response.status === 409) {
          alert('Nama provinsi sudah terdaftar.');
        }
      });
  };

  // add kabupaten
  const addKabupatenHandler = () => {
    if (provinsi.trim() === '') {
      // Display a warning message to the user
      alert('Nama provinsi tidak boleh kosong.');
      return;
    }
    if (kabupaten.trim() === '') {
      // Display a warning message to the user
      alert('Nama kabupaten tidak boleh kosong.');
      return;
    }
    axios
      .post(apiUrl+'/kabupaten', {
        nama_kabupaten: kabupaten,
        nama_provinsi: provinsi,
      })
      .then((res) => {
        console.log(res);
        window.location.reload();
      })
      .catch((error) => {
        if (error.response) {
          if (error.response.status === 409) {
            alert('Nama kabupaten sudah terdaftar.');
          }
        } else {
          alert('Nama provinsi tidak ditemukan.');
        }
      });
  };

  // add kecamatan
  const addKecamatanHandler = () => {
    if (kabupaten.trim() === '') {
      // Display a warning message to the user
      alert('Nama kabupaten tidak boleh kosong');
      return;
    }
    if (kecamatan.trim() === '') {
      // Display a warning message to the user
      alert('Nama kecamatan tidak boleh kosong');
      return;
    }
    axios
      .post(apiUrl+'/kecamatan', {
        nama_kecamatan: kecamatan,
        nama_kabupaten: kabupaten,
      })
      .then((res) => {
        console.log(res);
        window.location.reload();
      })
      .catch((error) => {
        if (error.response && error.response.status === 409) {
          alert('Nama kecamatan sudah terdaftar.');
        } else {
          alert('Nama Kabupaten tidak ditemukan');
        }
      });
  };

  // delete provinsi
  const deleteProvinsiHandler = () => {
    if (provinsi.trim() === '') {
      // Display a warning message to the user
      alert('Nama provinsi tidak boleh kosong');
      return;
    }
    axios
      .delete(apiUrl+`/provinsi/${provinsi}`, {
        nama_provinsi: provinsi,
      })
      .then((res) => {
        console.log(res);
        window.location.reload();
      })
      .catch((error) => {
        if (error.response) {
          if (error.response.status === 404) {
            alert('Nama provinsi tidak ditemukan.');
          } else {
            alert('Provinsi Masih memiliki kabupaten, tidak bisa dihapus.');
          }
        }
      });
  };

  const deleteKabupatenHandler = () => {
    if (kabupaten.trim() === '') {
      // Display a warning message to the user
      alert('Nama kabupaten tidak boleh kosong');
      return;
    }

    axios
      .delete(apiUrl+`/kabupaten/${kabupaten}`, {
        nama_kabupaten: kabupaten,
      })
      .then((res) => {
        console.log(res);
        window.location.reload();
      })
      .catch((error) => {
        if (error.response) {
          if (error.response.status === 404) {
            alert('Nama kabupaten tidak ditemukan.');
          } else {
            alert('Kabupaten Masih memiliki kecamatan, tidak bisa dihapus.');
          }
        }
      });
  };

  const deleteKecamatannHandler = () => {
    if (kecamatan.trim() === '') {
      // Display a warning message to the user
      alert('Nama kabupaten tidak boleh kosong');
      return;
    }

    axios
      .delete(apiUrl+`/kecamatan/${kecamatan}`, {
        nama_kecamatan: kecamatan,
      })
      .then((res) => {
        console.log(res);
        window.location.reload();
      })
      .catch((error) => {
        if (error.response) {
          if (error.response.status === 404) {
            alert('Nama kecamatan tidak ditemukan.');
          }
        }
      });
  };

  return (
    <div
      className="App list-Group-item justify-content-center align-items-center mx-auto"
      style={{
        width: isMobile ? '100%' : '100%',
      }}
    >
      <span className='justify-content-center align-items-center mx-auto mb-3' style={{display: 'flex', gap:'20px'}}>
        <img src={pic} style={{width: '100px'}}/>
        <h1 className="card text-white bg-secondary mb-3">Wilayah Indonesia</h1>
        <img src={pic} style={{width: '100px'}}/>
      </span>
      <div className="card-body">
        <span
          className="mb-3 justify-content-center  mx-auto"
          style={{ display: 'flex', gap: '10px' }}>
          
          <input
            className="form-control ProvIn"
            onChange={(event) => setProvinsi(event.target.value)}
            placeholder="Provinsi"
            style={{ width: isMobile ? '100%' : '300px' }}
          ></input>
          <button className="btn btn-outline-primary"
            style={{borderRadius: '50px', fontWeight: 'bold',width: '100px',}}
            onClick={addProvinsiHandler}>Add</button>
          <button className="btn btn-outline-primary"
            style={{borderRadius: '50px', fontWeight: 'bold', width: '100px',}}
            onClick={deleteProvinsiHandler}>Delete</button>
        </span>
        
        <span className="mb-3 justify-content-center align-items-center mx-auto" style={{ display: 'flex', gap: '10px' }}>
          <input
            className="form-control KabIn"
            onChange={(event) => setKabupaten(event.target.value)}
            placeholder="Kabupaten"
            style={{ width: isMobile ? '100%' : '300px' }}
          ></input>
          <button
            className="btn btn-outline-primary"
            style={{
              borderRadius: '50px',
              fontWeight: 'bold',
              width: '100px',
            }}
            onClick={addKabupatenHandler}
          >
            Add
          </button>
          <button
            className="btn btn-outline-primary"
            style={{
              borderRadius: '50px',
              fontWeight: 'bold',
              width: '100px',
            }}
            onClick={deleteKabupatenHandler}
          >
            Delete
          </button>
        </span>
        <span
          className="justify-content-center align-items-center mx-auto"
          style={{ display: 'flex', gap: '10px' }}
        >
          <input
            className="form-control KecIn"
            onChange={(event) => setKecamatan(event.target.value)}
            placeholder="Kecamatan"
            style={{ width: isMobile ? '100%' : '300px' }}
          ></input>
          <button
            className="btn btn-outline-primary"
            style={{
              borderRadius: '50px',
              fontWeight: 'bold',
              width: '100px',
            }}
            onClick={addKecamatanHandler}
          >
            Add
          </button>
          <button
            className="btn btn-outline-primary"
            style={{
              borderRadius: '50px',
              fontWeight: 'bold',
              width: '100px',
            }}
            onClick={deleteKecamatannHandler}
          >
            Delete
          </button>
        </span>
        <br></br>
        <h4 className="card text-white bg-secondary mb-3">Daftar Wilayah</h4>

        <div
          className=""
          style={{
            display: 'flex',
            flexDirection: isMobile ? 'column' : 'row',
            gap: '20px',
            alignItems: 'center',
          }}
        >
          <ProvinsiView provinsiList={provinsiList} />
          <KabupatenView kabupatenList={kabupatenList} />
          <KecamatanView
            kecamatanList={kecamatanList}
            kabupatenList={kabupatenList}
          />
        </div>
      </div>
    </div>
  );
}

export default App;
export {apiUrl};
