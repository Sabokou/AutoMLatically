import Papa from 'papaparse';

function CsvLoader(file, setCsvColumns, setCsvRows) {

    const loadCsvHeaders = (column_names) => {
      console.log('column_names', column_names)
      setCsvColumns(column_names)
    }

    const loadCsvRows = (row_list) => {
      console.log('row_list', row_list)
      setCsvRows(row_list)
    }
    
    const papaparseOptions = {
        worker: false,
        header: true,
        dynamicTyping: true,
        skipEmptyLines: true,
        preview: 100, // only load 100 rows of the csv file
        // maybe convert the headers ? -> but they would not be the same as the ones that are received in the backend
        // transformHeader: (header) =>
        //   header
        //     .toLowerCase()
        //     .replace(/\W/g, '_'),
        complete: (result, file) => {
          // read the header names from the first row in the csv data (= row)
          var column_names = result.meta.fields
          loadCsvHeaders(column_names)
          loadCsvRows(result.data)
        },
        error: (error, file) => {
            console.log('error:', error)
        }
      }
    console.log("starting the parse");
    Papa.parse(file, papaparseOptions)
}

export default CsvLoader