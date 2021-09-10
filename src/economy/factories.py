import factory
from django.utils import timezone

from .models import (
    Bank,
    BankAccount,
    BankTransaction,
    ClearhausSettlement,
    CoinifyBalance,
    CoinifyInvoice,
    CoinifyPayout,
    EpayTransaction,
)


class BankFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bank

    name = factory.Faker("company")


class BankAccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BankAccount

    bank = factory.Iterator(Bank.objects.all())
    name = factory.Faker("word")
    reg_no = factory.Faker("numerify", text="####")
    account_no = factory.Faker("numerify", text="########")


class BankTransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BankTransaction

    bank_account = factory.Iterator(BankAccount.objects.all())
    date = factory.Faker("date_between", start_date="-6y")
    text = factory.Faker("sentence")
    amount = factory.Faker(
        "pydecimal", right_digits=2, min_value=-100000, max_value=100000
    )
    balance = factory.Faker(
        "pydecimal", right_digits=2, min_value=-100000, max_value=100000
    )


class CoinifyInvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CoinifyInvoice

    coinify_id = factory.Faker("random_int", min=100000, max=200000)
    coinify_id_alpha = factory.Faker("pystr", min_chars=5, max_chars=8)
    coinify_created = factory.Faker(
        "date_time_between", start_date="-6y", tzinfo=timezone.utc
    )
    payment_amount = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=10000
    )
    payment_currency = "DKK"
    payment_btc_amount = factory.Faker(
        "pydecimal", right_digits=8, min_value=1, max_value=4
    )
    description = factory.Faker("sentence")
    custom = {}
    credited_amount = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=10000
    )
    credited_currency = "EUR"
    state = "complete"
    payment_type = factory.Faker(
        "random_element", elements=["normal", "normal", "extra"]
    )


class CoinifyPayoutFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CoinifyPayout

    coinify_id = factory.Faker("random_int", min=100000, max=200000)
    coinify_created = factory.Faker(
        "date_time_between", start_date="-6y", tzinfo=timezone.utc
    )
    amount = factory.Faker("pydecimal", right_digits=2, min_value=1000, max_value=10000)
    fee = factory.Faker("pydecimal", right_digits=2, min_value=1000, max_value=10000)
    transferred = factory.Faker(
        "pydecimal", right_digits=2, min_value=1000, max_value=10000
    )
    currency = "EUR"


class CoinifyBalanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CoinifyBalance

    date = factory.Faker("date_between", start_date="-6y")
    btc = factory.Faker("pydecimal", right_digits=8, min_value=1, max_value=4)
    dkk = factory.Faker("pydecimal", right_digits=2, min_value=100, max_value=10000)
    eur = factory.Faker("pydecimal", right_digits=2, min_value=100, max_value=10000)


class EpayTransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EpayTransaction

    merchant_id = "1024488"
    transaction_id = factory.Faker("random_int", min=100000, max=200000)
    order_id = factory.Faker("random_int", min=1000, max=2000)
    currency = "DKK"
    auth_date = factory.Faker(
        "date_time_between", start_date="-6y", tzinfo=timezone.utc
    )
    auth_amount = factory.Faker(
        "pydecimal", right_digits=2, min_value=500, max_value=3000
    )
    captured_date = factory.Faker(
        "date_time_between", start_date="-6y", tzinfo=timezone.utc
    )
    captured_amount = factory.Faker(
        "pydecimal", right_digits=2, min_value=500, max_value=3000
    )
    card_type = factory.Faker(
        "random_element",
        elements=[
            "Mastercard (udenlandsk)",
            "Visa/Electron (udenlandsk)",
            "Mastercard",
        ],
    )
    description = factory.Faker("sentence")
    transaction_fee = factory.Faker(
        "pydecimal", right_digits=2, min_value=2, max_value=5
    )


class ClearhausSettlementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ClearhausSettlement

    merchant_id = "2003656"
    merchant_name = "BornHack IVS"
    clearhaus_uuid = factory.Faker("uuid4")
    settled = factory.Faker("random_element", elements=[True, True, True, False])
    currency = "DKK"
    period_start_date = factory.Faker("date_between", start_date="-6y")
    period_end_date = factory.Faker("date_between", start_date="-6y")
    payout_amount = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    payout_date = factory.Faker("date_between", start_date="-6y")
    summary_sales = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    summary_credits = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    summary_refunds = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    summary_chargebacks = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    summary_fees = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    summary_other_postings = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    summary_net = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    reserve_amount = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    reserve_date = factory.Faker("date_between", start_date="-6y")
    fees_sales = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    fees_refunds = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    fees_authorisations = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    fees_credits = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    fees_minimum_processing = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    fees_service = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    fees_wire_transfer = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    fees_chargebacks = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    fees_retrieval_requests = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    payout_reference_number = factory.Faker("random_int", min=100000, max=200000)
    payout_descriptor = factory.Faker("sentence")
    reserve_reference_number = factory.Faker("random_int", min=100000, max=200000)
    reserve_descriptor = factory.Faker("sentence")
    fees_interchange = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )
    fees_scheme = factory.Faker(
        "pydecimal", right_digits=2, min_value=100, max_value=20000
    )