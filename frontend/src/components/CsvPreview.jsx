import React, { useMemo } from 'react'
import { useTable } from 'react-table'

import BTable from 'react-bootstrap/Table';

function Table({ columns, data }) {
    // Use the state and functions returned from useTable to build your UI
    const {
      getTableProps,
      getTableBodyProps,
      headerGroups,
      rows,
      prepareRow,
    } = useTable({
      columns,
      data,
    })
  
    // Render the UI for the bootstrap table according to this tutorial: https://codesandbox.io/s/o1pt2?file=/src/App.js
    return (
      <div>
      <BTable striped bordered hover size="sm" {...getTableProps()}>
        <thead>
          {headerGroups.map(headerGroup => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map(column => (
                <th {...column.getHeaderProps()}>{column.render('Header')}</th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody {...getTableBodyProps()}>
          {rows.map((row, i) => {
            prepareRow(row)
            return (
              <tr {...row.getRowProps()}>
                {row.cells.map(cell => {
                  return <td {...cell.getCellProps()}>{cell.render('Cell')}</td>
                })}
              </tr>
            )
          })}
        </tbody>
      </BTable>
      </div>
    )
  }

function CsvPreview({ column_data, row_data }) {
    // column and row data must be encoded into a useMemo hook, for the react-table
    const columns = useMemo(
        () => {
            // transform the column names into a list of objects that has the Header and accessor property, 
            // that is required by ract-table
            var column_transformed = []
            for(let i = 0; i < column_data.length; i++) {
                var column_name = column_data[i]
                column_transformed.push(
                    {
                        Header: column_name,
                        accessor: column_name
                    }
                )
            }
            return column_transformed
        },
        [column_data]
    )
    const rows = useMemo(
        () => {
            return row_data
        },
        [row_data]
    )

  return (
    <div>
      <div style={{color: "black", marginLeft: "15px"}}>Preview of up to 100 rows of the dataset:</div>
      <div style={{height: '30vh', width: "auto", backgroundColor: "white", borderRadius: "15px", margin: "15px", overflow: 'auto'}}>
          <Table columns={columns} data={rows} />
      </div>
    </div>
  )
}

export default CsvPreview