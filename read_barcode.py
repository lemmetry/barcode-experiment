def read_data_matrix(ucc):
    """
    Read the data matrix (medical) barcode and interpret its components: GTIN, serial number, expiration date, and lot
    number.
    'Application identifiers' are used to allow multiple data elements within a single barcode. In the data matrix
    the application identifiers codes go in this order: 01, 21, 17, then 10.
    See GS1 DataMatrix Guidelines for further details
    https://www.gs1.org/standards/gs1-datamatrix-guideline/25#2-Encoding-data+2-2-GS1-element-strings
    """
    identifiers = ['01', '21', '17', '10']
    identifiers_indices = []
    start_index = 0

    for identifier in identifiers:
        try:
            identifier_index = ucc.index(identifier, start_index)
            identifiers_indices.append(identifier_index)
            start_index = identifier_index
        except ValueError:
            print(f"Application identifier {identifier} not found")

    identifier_values = []
    for i in range(len(identifiers_indices) - 1):
        start = identifiers_indices[i] + 2
        end = identifiers_indices[i + 1]
        identifier_values.append(ucc[start:end])
    identifier_values.append(ucc[identifiers_indices[-1] + 2:])

    return identifier_values

barcode = input("Scan barcode: ")
values = read_data_matrix(barcode)

for i, j in zip(['GTIN', 'S/N', 'EXP', 'LOT'], values):
    print(i, j)
