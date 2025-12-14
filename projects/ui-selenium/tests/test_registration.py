from tests.conftest import new_user_data, fill_signup_form


def test_registration(
        open_home,
        open_signup,
        assert_register_btn_disabled,
        new_user_data,
        fill_signup_form,
        submit_signup,
        assert_registration_success
):
    pass