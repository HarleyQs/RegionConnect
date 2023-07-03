import ProvinsiItem from "./ProvinsiItem"





function ProvinsiView(props) {
    return (
      <div style={{ height: '400px', overflow: 'auto' }}>
        <table>
          <thead>
            <tr>
              <th colSpan='2'>Daftar Provinsi</th>
            </tr>
          </thead>
          <tbody>
            {props.provinsiList ? (
              props.provinsiList.map(provinsi => (
                <ProvinsiItem provinsi={provinsi} key={provinsi.nama_provinsi} />
              ))
            ) : (
              <tr>
                <td>Refresh until the list showed up</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    );
  }
  




export default ProvinsiView