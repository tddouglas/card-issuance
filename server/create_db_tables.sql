
CREATE TABLE IF NOT EXISTS cards (
   id bigserial PRIMARY KEY,
   payment_instrument_id VARCHAR (50) UNIQUE NOT NULL,
   cardholder_name VARCHAR (100) NOT NULL,
   status VARCHAR(255) UNIQUE NOT NULL,
   order_id bigint NOT NULL
   CONSTRAINT fk_order
   	  FOREIGN KEY(order_id)
   	  	REFERENCES orders(id)
);


CREATE TABLE IF NOT EXISTS logos (
   id bigserial PRIMARY KEY,
   url VARCHAR(2048) UNIQUE NOT NULL
);


CREATE TABLE IF NOT EXISTS approved_usecases (
   id bigserial PRIMARY KEY,
   country VARCHAR (100) UNIQUE NOT NULL,
   event_type VARCHAR (100) NOT NULL,
   spending_limit INT UNIQUE NOT NULL,
   allowed_countries VARCHAR(2048) NOT NULL,
   allowed_mccs VARCHAR(2048) NOT NULL,
   max_daily_spend INT NOT NULL,
   max_amount_per_transaction INT NOT NULL,
   payment_instrument_group_id VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS orders (
   id bigserial PRIMARY KEY,
   requesting_user VARCHAR (100) UNIQUE NOT NULL,
   number_of_cards INT NOT NULL,
   approved_usecase_id bigint UNIQUE NOT NULL,
   event_start_date TIMESTAMP NOT NULL,
   event_end_date TIMESTAMP NOT NULL,
   card_shipping_address VARCHAR(2048),
   shipping_status VARCHAR(512),
   logo_id bigint,
   CONSTRAINT fk_approved_usecase
   	  FOREIGN KEY(approved_usecase_id)
   	  	REFERENCES approved_usecases(id),
   CONSTRAINT fk_logo
   	  FOREIGN KEY(logo_id)
   	  	REFERENCES logos(id)
);

-- TODO maybe add some dummy data creation statements to make testing easier