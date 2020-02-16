# Test shopping cart

This is an executable specification file. This file follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

To execute this specification, run

    gauge run specs


## Increase quantity in cart and verify item quantity updated accordingly

* Login as a user
* Add 1 item to cart with quantity of 1
* Verify quantity is 1
* Increase quantity to 5
* Verify that quantity is updated to 5
* And total price is updated accordingly
