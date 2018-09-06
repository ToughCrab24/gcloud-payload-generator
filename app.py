# cli.py
import click
import base64
import json

@click.command()
@click.option('--purchase_id', '-i', prompt=True, default=1)
@click.option('--account_id', '-a', prompt=True, default=1)
@click.option('--customer_id', '-c', prompt=True, default=1)
@click.option('--product_id', '-p', prompt=True, default=1)
@click.option('--enabled', '-e', prompt=True, default=True)
def main(purchase_id, account_id, customer_id, product_id, enabled):

    pubsub = {
      "purchase_id": purchase_id,
      "account_id": account_id,
      "customer_id": customer_id,
      "product_id": product_id,
      "enabled": enabled,
    }
    # import pdb; pdb.set_trace()
    pubsub_json = json.dumps(pubsub).encode('ascii')

    b64encoded = base64.b64encode(pubsub_json)
    payload = {
      "message": {
        "attributes": {
          "key": "value"
        },
        "data": b64encoded.decode("utf-8"),
        "message_id": "136969346945"
      },
      "subscription": "projects/myproject/subscriptions/mysubscription"
    }

    click.secho(json.dumps(payload, sort_keys=True, indent=2), fg='green')

if __name__ == "__main__":
    main()