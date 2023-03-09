CREATE TABLE test-task-project-380016.raw_data.google_ads (
  date DATE,
  account_name STRING,
  cost FLOAT64
);
INSERT INTO test-task-project-380016.raw_data.google_ads (date, account_name, cost)
VALUES
  ('2023-02-25', 'Google Account 1', 85.25),
  ('2023-02-22', 'Google Account 2', 230.73169),
  ('2023-02-21', 'Google Account 3', 187.06),
  ('2023-02-20', 'Google Account 4', 223.39);
CREATE TABLE test-task-project-380016.raw_data.yandex_direct (
  date DATE,
  account_name STRING,
  cost FLOAT64
);
INSERT INTO test-task-project-380016.raw_data.yandex_direct (date, account_name, cost)
VALUES
  ('2023-02-21', 'Yandex Account 1', 85.25),
  ('2023-02-22', 'Yandex Account 2', 230.73169),
  ('2023-02-25', 'Yandex Account 3', 187.06),
  ('2023-02-26', 'Yandex Account 4', 223.39);

CREATE TABLE est-task-project-380016.crm_deals (
  date_create DATE,
  account_name STRING,
  stage_of_lead STRING
);
INSERT INTO mydataset.mytable (`Date Create`, `Account Name`, `Stage of lead`)
VALUES
  ('2023-02-21', 'Yandex Account 1', 'New'),
  ('2023-02-23', 'Yandex Account 2', 'In progress'),
  ('2023-02-22', 'Google Account 2', 'Junk');
