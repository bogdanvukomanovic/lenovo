package com.example.repositories;

import com.example.model.Account;
import com.example.repositories.mappers.AccountRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.math.BigDecimal;
import java.util.List;

@Repository
public class AccountRepository {

    private final JdbcTemplate jdbc;

    public AccountRepository(JdbcTemplate jdbc) {
        this.jdbc = jdbc;
    }

    public Account findAccountById(long id) {
        return jdbc.queryForObject("SELECT * FROM account WHERE id = ?", new AccountRowMapper(), id);
    }

    public void changeAmount(long id, BigDecimal amount) {
        jdbc.update("UPDATE account SET amount = ? WHERE id = ?", amount, id);
    }

    public List<Account> findAllAccounts() {
        return jdbc.query("SELECT * FROM account", new AccountRowMapper());
    }

}
