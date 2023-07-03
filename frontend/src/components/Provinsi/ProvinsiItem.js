import React, {useState} from "react";
import axios from "axios";
import { apiUrl } from "../../App";





function ProvinsiItem(props) {
    const old_value = props.provinsi.nama_provinsi;
    const [editing, setEditing] = useState(false);
    const [newProvinsi, setNewProvinsi] = useState(props.provinsi.nama_provinsi);
  
    const handleEdit = () => {
        if (newProvinsi ===''){
            alert("Nama provinsi tidak bisa kosong");
            return;
        }
      axios
        .put(apiUrl+`/provinsi/${old_value}`, {
          nama_provinsi: newProvinsi,
          new_info: old_value,
        })
        .then((res) => {
          console.log(res);
          console.log('Update province:', newProvinsi, 'old provinsi', old_value);
          setEditing(false);
          window.location.reload();
        })
        .catch((error) => {
          alert("Provinsi memiliki kabupaten atau suda terdaftar, tidak bisa diubah.");
          window.location.reload();
        });

    };
  
    return (
        
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
            </td>
            <td>
              <button style={{borderRadius:'50px'}} onClick={handleEdit}>Save</button>
            </td>
          </>
        ) : (
          <>
            <td style={{ whiteSpace: 'pre-wrap' }}>{props.provinsi.nama_provinsi}</td>
            <td>
              <button style={{borderRadius:'50px'}} onClick={() => setEditing(true)}>Edit</button>
            </td>
          </>
        )}
      </tr>
    );
  }
  

export default ProvinsiItem