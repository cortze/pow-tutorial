import hashlib
import argparse
import json
import time


def main(args):
    # Check if the input file was provided
    if not args.input:
        print('no input file was given')
        exit(0)
    if not args.difficulty:
        print('no difficulty was given')
        exit(0)

    # Generate a block object that later gets filled from given .json file
    block = Block()
    block.import_from_json(args.input)

    # Calculate nonce to make the block valid
    valid_block = calculate_valid_block(block, args.difficulty)
    print(valid_block.get_json())

def get_diff_mask(bit_base, diff):
    # fill a variable of '1' and make the variable to shift dif times << so that '11111111000'
    # apply the mask with an 'OR' comparison and if the result matches de mask, ok!
    diff_mask = (1 << bit_base) - 1# assuming that int in python is int64
    diff_mask = diff_mask << diff
    # bring the len of the mask back to 64 bits
    diff_mask = 0xFFFFFFFFFFFF & diff_mask
    return diff_mask


def calculate_valid_block(block, diff):
    """
    Completar los campos que faltan en la función `calculate_valid_block()` de manera que 
    esta devuelva el objeto Block con un valor de `nonce` valido para que el hash del bloque 
    tenga `X` número de ceros por la derecha. (donde X es la dificultad definida al llamar al script)

    NOTA: Comparadores binarios:
    or -> `|` 
    1111 | 0000 = 1111
    and -> `&`
    1010 & 0101 = 0000
    """

    # Get the base mask that will determine if the hash of the block is valid or not 
    diff_mask = get_diff_mask(64, diff)
    

    ## --- Espacio para rellenar ---

    hash = ....

    while .... :

        time.sleep(1)
        
 
    ## --- Fin de espacio ---

    print('block successfully mined at nonce', block.nonce)
    print('hash hex:         ', hex(hash))
    print('matching mask hex:', hex(diff_mask))
    print('hash bin:         ', bin(hash))
    print('matching mask bin:', bin(diff_mask))

    return block

class Block():
    
    def __init__(self):
        self.block_number = 0
        self.parent_block = 0
        self.nonce = 0
        self.transactions = []

    def import_from_json(self, file):
        print('loading json file', file)
        # read the json file
        f = open(file, 'r')
        data = json.load(f)
        # compose local struct from json
        self.block_number = data["header"]["block_number"]
        self.parent_block = data["header"]["parent_block"]
        self.nonce = data["header"]["nonce"]
        # import transactions
        for trans in data["body"]["transactions"]:
            t = Transaction(trans["from"], trans["to"], trans["amount"])
            self.transactions.append(t)
        print('block loaded:\n', self.get_json())

        f.close()

    def get_json(self):
        # Rebuild the json from local block info
        block_dict = {
            "header": {
                "block_number": self.block_number,
                "parent_block": self.parent_block,
                "nonce": self.nonce,
            },
            "body": {
                "transactions": [],
            },
        }
        for trans in self.transactions:
            block_dict["body"]["transactions"].append(trans.get_json())
        # TODO: necessary to generate a new file? (json.dump)
        return json.dumps(block_dict).encode("utf-8")

    def increase_nonce(self):
        """
        Completar la funcion increase_nonce() de manera que se incremente
        el valor de la variable `nonce` del objeto Block.
        """
        ## --- Espacio para rellenar ---


        ## --- Fin de espacio ---

    def get_hash(self):
        """
        Completar la funcion get_hash() del objeto Block para que devuelva el 
        valor hash de la version serializada del bloque.

        Para ello se deberá usar la función `sha256` de la librería `hashlib`

        NOTA: La función contiene 2 líneas extra que se encarga de simplificar 
        el tamaño de las variables que luego se van a usar. Se recomienda no tocar
        nada fuera del espacio asignado para rellenar.
        """

        ## --- Espacio para rellenar ---
        

        ## --- Fin de espacio ---

        # Do not touch 
        # Format the hash value into an integer 
        # Apply 64 bit mask to simplify mask operators 
        hash = int('0x'+hash.hexdigest(), 0)
        hash = 0xFFFFFFFFFFFF & hash   
        return hash
    
    
    def check_valid_transactions(self, balances):
        ## Ejercicio 2
        """
        Esta función debe iterar sobre la lista de transacciones del bloque y revisar que son válidas.
        En caso de que una transacción no sea válida se debe retornar Falso.
        En cualquier otro caso se debe retornar Verdadero.
        """
        balances_copy = balances.copy() # hacemos una copia para no modificar la variable original
        ## --- Espacio para rellenar ---
        

        ## --- Fin de espacio ---

        return True

class Transaction():
    t_from = ""
    t_to = ""
    t_amount = 0

    def __init__(self, t_from, t_to, t_amount):
        self.t_from = t_from
        self.t_to = t_to
        self.t_amount = t_amount
    
    # TODO: Could be nice to implement something like that to see if they are valid
    def valid(self, input_balances):
        ## Ejercicio 2
        """
        Esta función debe revisar que la transacción es válida teniendo en cuenta el diccionario de balances que 
        se recibe por argumentos.
        Una transacción es válida siempre "t_from" tiene fondos suficientes en "input_balances" para traspasar "t_amount".
        La función retorna Verdadero en caso de que la transacción sea válida, y Falso en caso de que no.
        """

        ## --- Espacio para rellenar ---
        
        ## --- Fin de espacio ---

        return True

    def get_json(self):
        return {
            "from": self.t_from,
            "to": self.t_to,
            "amount": self.t_amount,
        }

def import_balances(input_file):
    ## Ejercicio 2

    """
    This method will import a json containing the balances of the different participants of the blockchain
    """
    # read the json file
    print('loading json file', input_file)
    f = open(input_file, 'r') # open in read mode
    data = json.load(f) # load json format
    print('balances loaded:\n', data)
    return data

if __name__ == "__main__":
    # parse arguments
    parser = argparse.ArgumentParser(description='PoW example')
    parser.add_argument('--input', type=str,
                        help='input file to generate the hash')
    parser.add_argument('--difficulty', type=int, 
                        help='define the dificulty level of PoW')
    args = parser.parse_args()
    main(args)
