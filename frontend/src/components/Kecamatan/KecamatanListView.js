import KecamatanItem from "./KecamatanItem";

function KecamatanView(props) {
    return (
      <div style={{ height: '400px', overflow: 'auto' }}>
        <table>
            <thead>
                <tr>
                    <th colSpan='2'>Daftar Kecamatan</th>
                </tr>
            </thead>
            <tbody >
            {props.kecamatanList.map((kecamatan) => {
            const kabupaten = props.kabupatenList.find((kab) => kab.nama_kabupaten === kecamatan.nama_kabupaten);
            return (
              <KecamatanItem kecamatan={kecamatan} kabupaten={kabupaten} key={kecamatan.nama_kecamatan} />
            );
          })}
            </tbody>
        </table>
      </div>
    );
  } 

export default KecamatanView