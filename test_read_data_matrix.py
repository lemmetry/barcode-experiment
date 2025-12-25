import unittest
from read_barcode import read_data_matrix

class TestBarcode(unittest.TestCase):

    def test_barcode_length(self):
        barcodes = [
            '0100367457153032212HA3CX2GPA17270630103246770',  # Amiodarone
            '0100351662128220172702282110867927044410A1009522',  # NTG
            '010037248551010821Y05X68FCCVNXHB172804301090001269',  # TXA
            '010036050561305221136183891727113010HB3B4217',  # Ondansetron
            '0100370069021255218564326343961310E052A11417270228',  # Dexamethasone
            '0100372603251258212016001847771728053110E210A001',  # Lasix
            '010037620410001421100001060370172707311025HD9',  # Atrovent
        ]

        for barcode in barcodes:
            barcode_components = read_data_matrix(barcode)

            barcode_components_length = 0
            for barcode_component in barcode_components:
                barcode_components_length += len(barcode_component)
            barcode_components_length += 8  # length of '01', '21', '17' and '10'

            self.assertEqual(len(barcode), barcode_components_length, msg=f'{barcode}, {barcode_components}')

if __name__ == '__main__':
    unittest.main()
