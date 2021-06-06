CREATE DATABASE news_main;

CREATE TABLE news_main.m_news (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  description VARCHAR(255),
  create_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  INDEX id_index (id)
  );

INSERT news_main.m_news (name, description) VALUES ('テスト', 'テストです');
INSERT news_main.m_news (name, description) VALUES ('テスト2', 'テスト2です');

SELECT * FROM news_main.m_news;