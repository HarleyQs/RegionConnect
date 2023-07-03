import React, {useState} from "react";
import axios from "axios";
import { apiUrl } from "../../App";



function KabupatenItem(props){
  
    const old_value_kabuapten = props.kabupaten.nama_kabupaten;
    // const old_value_provinsi = props.kabupaten.nama_provinsi;
    const [editing, setEditing] = useState(false);
    const [newProvinsi, setNewProvinsi] = useState(props.kabupaten.nama_provinsi);
    const [newKabupaten, setNewKabupaten] = useState(props.kabupaten.nama_kabupaten);

    const handleEdit = () => {
        if (newProvinsi ===''){
            alert("Nama provinsi tidak bisa kosong");
            return;
        }
        if (newKabupaten ===''){
            alert("Nama kabupaten tidak bisa kosong");
            return;
        }
      axios
        .put(apiUrl+`/kabupaten/${old_value_kabuapten}`, {
          nama_kabupaten: newKabupaten,
        //   new_info: {"nama_kabupaten":newKabupaten, "nama_provinsi":newProvinsi} 
          nama_provinsi: newProvinsi
        })
        .then((res) => {
          console.log(res.data);
          console.log('new_provinsi:', newProvinsi, 'new_kabupaten:', newKabupaten);
          setEditing(false);
          window.location.reload();
        })
        .catch((error) => {
          alert("Kabupaten memiliki kecamatan atau sudah terdaftar, tidak bisa diubah.");
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
                value={newProvinsi}
                onChange={(e) => setNewProvinsi(e.target.value)}
                // onBlur={handleEdit}
              />
              <input
              type="text"
              value={newKabupaten}
              onChange={(e) => setNewKabupaten(e.target.value)}
            //   onBlur={handleEdit}
              />
            </td>
            <td>
              <button style={{borderRadius:'50px'}} onClick={handleEdit}>Save</button>
            </td>
          </>
        ) : (
          <>
            <td>{props.kabupaten.nama_provinsi}, {props.kabupaten.nama_kabupaten}</td>
            <td>
              <button style={{borderRadius:'50px'}} onClick={() => setEditing(true)}>Edit</button>
            </td>
          </>
        )}
      </tr>
    );
}

export default KabupatenItem