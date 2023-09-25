def get_payment_instruments_request(test_mode: bool, approved_usecase_id):
    # Return TEST /paymentInstruments creation request
    if test_mode:
        # return {
        #     "type": "card",
        #     "description": "Adyen Event" + str(approved_usecase_id),
        #     "status": "Requested",
        #     "issuingCountryCode": "US",
        #     "balanceAccountId": "BA3227C223222B5G9WQBZ9VS8",
        #     "paymentInstrumentGroupId": "PG32272223222L5JJL6WVFB3N",
        #     "card": {
        #         "formFactor": "physical",
        #         "brand": "mc",
        #         "brandVariant": "mc_debit_mco",
        #         "cardholderName": "Adyen Event",
        #         "configuration": {
        #             "configurationProfileId": "CP32272223222H5HWFJXN9Z9Z",
        #             "bulkAddress": {
        #                 "city": "Amsterdam",
        #                 "company": "Adyen",
        #                 "country": "NL",
        #                 "houseNumberOrName": "49",
        #                 "postalCode": "1012 KK",
        #                 "street": "Rokin"
        #             },
        #             "shipmentMethod": "nationalDhlBulk",
        #         },
        #         "deliveryContact": {
        #             "address": {
        #                 "city": "Amsterdam",
        #                 "country": "NL",
        #                 "line1": "Rokin 49",
        #                 "postalCode": "1012 KK",
        #             },
        #             "name": {
        #                 "firstName": "Adyen",
        #                 "lastName": "Card"
        #             }
        #         }
        #     }
        # }
        return {
            "type": "card",
            "description": "My test card",
            "balanceAccountId": "BA3227C223222B5G9WQBZ9VS8",
            "issuingCountryCode": "US",
            "card": {
                "cardholderName": "Simon Hopper",
                "brand": "mc",
                "brandVariant": "mc_credit_mco",
                "formFactor": "virtual"
            }
        }
    else:
        # Return LIVE /paymentInstruments creation request
        return {
            "type": "card",
            "description": "Adyen Event" + approved_usecase_id,
            "status": "inactive",
            "issuingCountryCode": "US",
            "balanceAccountId": "BA3227C223222B5G9WQBZ9VS8",
            "paymentInstrumentGroupId": "PG32272223222L5JJL6WVFB3N",
            "card": {
                "formFactor": "physical",
                "brand": "mc",
                "brandVariant": "mc_debit_mdt",
                "cardholderName": "Cardholder Name",
                "configuration": {
                    "configurationProfileId": "CP123",
                    "bulkAddress": {
                        "city": "Amsterdam",
                        "company": "Adyen",
                        "country": "NL",
                        "houseNumberOrName": "49",
                        "postalCode": "1012 KK",
                        "street": "Rokin"
                    },
                    "shipmentMethod": "nationalDhlBulk",
                },
                "deliveryContact": {
                    "address": {
                        "city": "Amsterdam",
                        "country": "NL",
                        "line1": "Rokin 49",
                        "postalCode": "1012 KK",
                    },
                    "name": {
                        "firstName": "Adyen",
                        "lastName": "Card"
                    }
                }
            }
        }
