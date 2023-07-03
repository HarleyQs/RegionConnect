import React, {useState} from "react";
import axios from "axios";
import { apiUrl } from "../../App";

function KecamatanItem(props){

    const old_value_kecamatan = props.kecamatan.nama_kecamatan;
    // const old_value_provinsi = props.kabupaten.nama_provinsi;
    const [editing, setEditing] = useState(false);
    const [newkecamatan, setNewKecamatan] = useState(props.kecamatan.nama_kecamatan);
    const [newKabupaten, setNewKabupaten] = useState(props.kecamatan.nama_kabupaten);

    const handleEdit = () => {
        if (newKabupaten ===''){
            alert("Nama Kabupaten tidak bisa kosong");
            return;
        }
        if (newkecamatan ===''){
            alert("Nama Kecamatan tidak bisa kosong");
            return;
        }
      axios
        .put(apiUrl+`/kecamatan/${old_value_kecamatan}`, {
          nama_kabupaten: newKabupaten,
        //   new_info: {"nama_kabupaten":newKabupaten, "nama_provinsi":newProvinsi} 
          nama_kecamatan: newkecamatan
        })
        .then((res) => {
          console.log(res.data);
          console.log('new_kabupaten:', newKabupaten, 'new_kecamatan:', newkecamatan);
          setEditing(false);
          window.location.reload();
        })
        .catch((error) => {
          alert(error.data);
          window.location.reload();
        });

    };
  

    return(
        <tr>
        {editing ? (
          <>
            <td>
              <input
                type="text"
                value={newKabupaten}
                onChange={(e) => setNewKabupaten(e.target.value)}
                // onBlur={handleEdit}
              />
              <input
              type="text"
              value={newkecamatan}
              onChange={(e) => setNewKecamatan(e.target.value)}
            //   onBlur={handleEdit}
              />
            </td>
            <td>
              <button style={{borderRadius:'50px'}} onClick={handleEdit}>Save</button>
            </td>
          </>
        ) : (
          <>
            <td><td style={{fontWeight: 'bold, underline'}}> {props.kabupaten.nama_provinsi}, {props.kabupaten.nama_kabupaten}, {props.kecamatan.nama_kecamatan}</td></td>
            <td>
              <button style={{borderRadius:'50px'}} onClick={() => setEditing(true)}>Edit</button>
            </td>
          </>
        )}
      </tr>
    );
}




export default KecamatanItem