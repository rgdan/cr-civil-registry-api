# Costa Rica National Registry API

API written in Python to get info from [Costa Rica's national registry website](https://servicioselectorales.tse.go.cr/chc/).

## Usage

### ID

Get information from the registry's website from an ID number.

#### Example

```
https://example.com/id_lookup?id=000000000
```

```
{
  "alias": " ",
  "birthday": "15/12/1986",
  "death_date": "",
  "father": "FREDDY ANTONIO NAVAS VIQUEZ",
  "father_id_number": "0",
  "full_name": "KEILOR ANTONIO NAVAS  GAMBOA",
  "homeless": "NO",
  "id_number": "113000998",
  "mother": "SANDRA GAMBOA GUZMAN",
  "mother_id_number": "106910100",
  "nationality": "COSTARRICENSE"
}
```

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
