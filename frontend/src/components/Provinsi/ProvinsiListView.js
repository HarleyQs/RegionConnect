import ProvinsiItem from "./ProvinsiItem"





function ProvinsiView(props){
    return(
        <div style={{ height: '400px', overflow: 'auto' }}>
            <table>
                <thead>
                    <tr>
                        <th colSpan='2'>Daftar Provinsi</th>
                    </tr>
                </thead>
                <tbody>
                {props.provinsiList.map(provinsi => <ProvinsiItem provinsi={provinsi} key={provinsi.nama_provinsi}/>)}
                </tbody>
            </table>
        </div>
    )
}




export default ProvinsiView