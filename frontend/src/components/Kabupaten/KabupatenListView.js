import KabupatenItem from "./KabupatenItem"


function KabupatenView(props){
    return(
        <div style={{ height: '400px', overflow: 'auto' }}>
            <table>
                <thead>
                    <tr>
                        <th colSpan='2'>Daftar Kabupaten</th>
                    </tr>
                </thead>
                <tbody>
                {props.kabupatenList.map(kabupaten => <KabupatenItem kabupaten={kabupaten} key={kabupaten.nama_kabupaten}/>)}
                </tbody>
            </table>
        </div>
    )
}

export default KabupatenView