# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

@blueprint.route('/index')

def index():
    return render_template('pages/dashboard/index.html')

# Demo pages
@blueprint.route('/dashboard/analytics/')
def analytics():
    return render_template('pages/dashboard/analytics.html')

@blueprint.route('/application/team/')
def team():
  return render_template('pages/application/team-v2.html')

@blueprint.route('/application/team/kathy')
def team_kathie():
  return render_template('pages/application/profile-kathy.html')

@blueprint.route('/application/team/brian')
def team_brian():
  return render_template('pages/application/profile-brian.html')

@blueprint.route('/application/team/ellie')
def team_ellie():
  return render_template('pages/application/profile-ellie.html')

@blueprint.route('/application/team/may')
def team_may():
  return render_template('pages/application/profile-may.html')

@blueprint.route('/application/team/matt')
def team_matt():
  return render_template('pages/application/profile-matt.html')

@blueprint.route('/application/team/tash')
def team_tash():
  return render_template('pages/application/profile-tash.html')

# Dashboard
@blueprint.route('/dashboard-index')
def dashboard_index():
    return render_template('pages/dashboard/index.html')

# Widgets
@blueprint.route('/widgets/statistics/')
def statistics():
  return render_template('pages/widgets/statistics.html')

@blueprint.route('/widgets/data/')
def data():
  return render_template('pages/widgets/data.html')

@blueprint.route('/widgets/chart/')
def chart():
  return render_template('pages/widgets/chart.html')

# Layout
@blueprint.route('/layout/vertical/')
def vertical_layout():
  return render_template('pages/demo/layout-vertical.html')

@blueprint.route('/layout/horizontal/')
def horizontal_layout():
  return render_template('pages/demo/layout-horizontal.html')

@blueprint.route('/layout/compact/')
def compact_layout():
  return render_template('pages/demo/layout-compact.html')

# Application
@blueprint.route('/application/social-profile')
def social_profile():
  return render_template('pages/application/social-profile.html')

@blueprint.route('/application/account-profile-v1')
def account_profile_v1():
  return render_template('pages/application/account-profile-v1.html')

@blueprint.route('/application/account-profile-v2')
def account_profile_v2():
  return render_template('pages/application/account-profile-v2.html')

@blueprint.route('/application/account-profile-v3')
def account_profile_v3():
  return render_template('pages/application/account-profile-v3.html')

# Card
@blueprint.route('/application/user-card-v1/')
def user_card_v1():
  return render_template('pages/application/user-card-v1.html')

@blueprint.route('/application/user-card-v2/')
def user_card_v2():
  return render_template('pages/application/user-card-v2.html')

@blueprint.route('/application/user-card-v3/')
def user_card_v3():
  return render_template('pages/application/user-card-v3.html')

# List


@blueprint.route('/application/user-list-v2/')
def user_list_v2():
  return render_template('pages/application/user-list-v2.html')

# Customer
@blueprint.route('/application/customer-list/')
def customer_list():
  return render_template('pages/application/cust_customer_list.html')

@blueprint.route('/application/order-list/')
def order_list():
  return render_template('pages/application/cust_order_list.html')

@blueprint.route('/application/create-invoice/')
def create_invoice():
  return render_template('pages/application/cust_create_invoice.html')

@blueprint.route('/application/order-details/')
def order_details():
  return render_template('pages/application/cust_order_details.html')

@blueprint.route('/application/product-list/')
def product_list():
  return render_template('pages/application/cust_product_list.html')

@blueprint.route('/application/product-review/')
def product_review():
  return render_template('pages/application/cust_product_review.html')

@blueprint.route('/application/chat/')
def chat():
  return render_template('pages/application/chat.html')

@blueprint.route('/application/kanban/')
def kanban():
  return render_template('pages/application/kanban.html')

@blueprint.route('/application/mail/')
def mail():
  return render_template('pages/application/mail.html')

@blueprint.route('/application/calendar/')
def calendar():
  return render_template('pages/application/calendar.html')

@blueprint.route('/application/contact-cards/')
def contact_cards():
  return render_template('pages/application/contact_cards.html')

@blueprint.route('/application/customer/')
def customer():
  return render_template('pages/application/customer.html')

# Ecommerce
@blueprint.route('/application/ecommerce-product/')
def ecom_product():
  return render_template('pages/application/ecom_product.html')

@blueprint.route('/application/ecommerce-product-details/')
def ecom_product_details():
  return render_template('pages/application/ecom_product-details.html')

@blueprint.route('/application/ecommerce-product-list/')
def ecom_product_list():
  return render_template('pages/application/ecom_product-list.html')

@blueprint.route('/application/ecommerce-checkout/')
def ecom_checkout():
  return render_template('pages/application/ecom_checkout.html')


# Basic Elements
@blueprint.route('/elements/alerts/')
def alerts():
  return render_template('pages/elements/bc_alert.html')

@blueprint.route('/elements/badges/')
def badges():
  return render_template('pages/elements/bc_badges.html')

@blueprint.route('/elements/breadcrumb-pagination/')
def breadcrumb_pagination():
  return render_template('pages/elements/bc_breadcrumb-pagination.html')

@blueprint.route('/elements/button/')
def button():
  return render_template('pages/elements/bc_button.html')

@blueprint.route('/elements/card/')
def card():
  return render_template('pages/elements/bc_card.html')

@blueprint.route('/elements/carousel/')
def carousel():
  return render_template('pages/elements/bc_carousel.html')

@blueprint.route('/elements/collapse/')
def collapse():
  return render_template('pages/elements/bc_collapse.html')

@blueprint.route('/elements/color/')
def color():
  return render_template('pages/elements/bc_color.html')

@blueprint.route('/elements/dropdowns/')
def dropdowns():
  return render_template('pages/elements/bc_dropdowns.html')

@blueprint.route('/elements/extra/')
def extra():
  return render_template('pages/elements/bc_extra.html')

@blueprint.route('/elements/grid/')
def grid():
  return render_template('pages/elements/bc_grid.html')

@blueprint.route('/elements/list-group/')
def list_group():
  return render_template('pages/elements/bc_list-group.html')

@blueprint.route('/elements/modal/')
def modal():
  return render_template('pages/elements/bc_modal.html')

@blueprint.route('/elements/offcanvas/')
def offcanvas():
  return render_template('pages/elements/bc_offcanvas.html')

@blueprint.route('/elements/progress/')
def progress():
  return render_template('pages/elements/bc_progress.html')

@blueprint.route('/elements/spinner/')
def spinner():
  return render_template('pages/elements/bc_spinner.html')

@blueprint.route('/elements/tabs/')
def tabs():
  return render_template('pages/elements/bc_tabs.html')

@blueprint.route('/elements/toasts/')
def toasts():
  return render_template('pages/elements/bc_toasts.html')

@blueprint.route('/elements/tooltip-popover/')
def tooltip_popover():
  return render_template('pages/elements/bc_tooltip-popover.html')

@blueprint.route('/elements/typography/')
def typography():
  return render_template('pages/elements/bc_typography.html')



# Advance Elements
@blueprint.route('/elements/sweet-alert/')
def sweet_alert():
  return render_template('pages/elements/ac_alert.html')

@blueprint.route('/elements/datepicker/')
def datepicker():
  return render_template('pages/elements/ac_datepicker-componant.html')

@blueprint.route('/elements/lightbox/')
def lightbox():
  return render_template('pages/elements/ac_lightbox.html')

@blueprint.route('/elements/ac-modal/')
def ac_modal():
  return render_template('pages/elements/ac_modal.html')

@blueprint.route('/elements/notification/')
def notification():
  return render_template('pages/elements/ac_notification.html')

@blueprint.route('/elements/range-slider/')
def range_slider():
  return render_template('pages/elements/ac_rangeslider.html')

@blueprint.route('/elements/slider/')
def slider():
  return render_template('pages/elements/ac_slider.html')

@blueprint.route('/elements/syntax-highlighter/')
def syntax_highlighter():
  return render_template('pages/elements/ac_syntax_highlighter.html')

@blueprint.route('/elements/tour/')
def tour():
  return render_template('pages/elements/ac_tour.html')

@blueprint.route('/elements/tree-view/')
def tree_view():
  return render_template('pages/elements/ac_treeview.html')


# Icons
@blueprint.route('/elements/feather/')
def feather():
  return render_template('pages/elements/icon-feather.html')

@blueprint.route('/elements/fontawesome/')
def font_awesome():
  return render_template('pages/elements/icon-fontawesome.html')

@blueprint.route('/elements/material/')
def material():
  return render_template('pages/elements/icon-material.html')

@blueprint.route('/elements/tabler/')
def tabler():
  return render_template('pages/elements/icon-tabler.html')


# Forms
@blueprint.route('/forms/form-basic/')
def form_elements():
  return render_template('pages/forms/form_elements.html')

@blueprint.route('/forms/form-floating/')
def form_floating():
  return render_template('pages/forms/form_floating.html')

@blueprint.route('/forms/form-options/')
def form_options():
  return render_template('pages/forms/form2_basic.html')

@blueprint.route('/forms/input-groups/')
def input_groups():
  return render_template('pages/forms/form2_input_group.html')

@blueprint.route('/forms/checkbox/')
def checkbox():
  return render_template('pages/forms/form2_checkbox.html')

@blueprint.route('/forms/radio/')
def radio():
  return render_template('pages/forms/form2_radio.html')

@blueprint.route('/forms/switch/')
def switch():
  return render_template('pages/forms/form2_switch.html')

@blueprint.route('/forms/mega-option/')
def mega_option():
  return render_template('pages/forms/form2_megaoption.html')

@blueprint.route('/forms/form-datepicker/')
def form_datepicker():
  return render_template('pages/forms/form2_datepicker.html')

@blueprint.route('/forms/date-range-picker/')
def date_range_picker():
  return render_template('pages/forms/form2_daterangepicker.html')

@blueprint.route('/forms/time-picker/')
def timepicker():
  return render_template('pages/forms/form2_timepicker.html')

@blueprint.route('/forms/form-choices/')
def form_choices():
  return render_template('pages/forms/form2_choices.html')

@blueprint.route('/forms/recaptcha/')
def recaptcha():
  return render_template('pages/forms/form2_recaptcha.html')

@blueprint.route('/forms/input-mask/')
def input_mask():
  return render_template('pages/forms/form2_inputmask.html')

@blueprint.route('/forms/clipboard/')
def clipboard():
  return render_template('pages/forms/form2_clipboard.html')

@blueprint.route('/forms/nouislider/')
def nouislider():
  return render_template('pages/forms/form2_nouislider.html')

@blueprint.route('/forms/bootstrap-switch/')
def bootstrap_switch():
  return render_template('pages/forms/form2_switchjs.html')

@blueprint.route('/forms/typeahead/')
def typeahead():
  return render_template('pages/forms/form2_typeahead.html')


# Text Editors
@blueprint.route('/forms/tinymce/')
def tinymce():
  return render_template('pages/forms/form2_tinymce.html')

@blueprint.route('/forms/quill/')
def quill():
  return render_template('pages/forms/form2_quill.html')

@blueprint.route('/forms/ckeditor-classic/')
def ck_editor_classic():
  return render_template('pages/forms/editor-classic.html')

@blueprint.route('/forms/ckeditor-document/')
def ck_editor_document():
  return render_template('pages/forms/editor-document.html')

@blueprint.route('/forms/ckeditor-inline/')
def ck_editor_inline():
  return render_template('pages/forms/editor-inline.html')

@blueprint.route('/forms/ckeditor-balloon/')
def ck_editor_balloon():
  return render_template('pages/forms/editor-balloon.html')

@blueprint.route('/forms/markdown/')
def markdown():
  return render_template('pages/forms/form2_markdown.html')


# Form Layout
@blueprint.route('/form/default-layout/')
def form_layout():
  return render_template('pages/forms/form2_lay-default.html')

@blueprint.route('/form/multicolumn/')
def multicolumn():
  return render_template('pages/forms/form2_lay-multicolumn.html')

@blueprint.route('/form/action-bars/')
def action_bars():
  return render_template('pages/forms/form2_lay-actionbars.html')

@blueprint.route('/form/sticky-action-bars/')
def sticky_action_bars():
  return render_template('pages/forms/form2_lay-stickyactionbars.html')


# File Upload
@blueprint.route('/form/dropzone/')
def dropzone():
  return render_template('pages/forms/file-upload.html')

@blueprint.route('/form/uppy/')
def uppy():
  return render_template('pages/forms/form2_flu-uppy.html')

@blueprint.route('/form/form-validation/')
def form_validation():
  return render_template('pages/forms/form-validation.html')

@blueprint.route('/form/image-cropper/')
def image_cropper():
  return render_template('pages/forms/image_crop.html')

# Table
@blueprint.route('/table/basic-table/')
def basic_table():
  return render_template('pages/table/tbl_bootstrap.html')

@blueprint.route('/table/sizing-table/')
def sizing_table():
  return render_template('pages/table/tbl_sizing.html')

@blueprint.route('/table/border-table/')
def border_table():
  return render_template('pages/table/tbl_border.html')

@blueprint.route('/table/styling-table/')
def styling_table():
  return render_template('pages/table/tbl_styling.html')

# Vanilla Table
@blueprint.route('/table/basic-initialization/')
def basic_initialization():
  return render_template('pages/table/tbl_dt-simple.html')

@blueprint.route('/table/dynamic-import/')
def dynamic_import():
  return render_template('pages/table/tbl_dt-dynamic-import.html')

@blueprint.route('/table/render-column-cells/')
def render_column_cells():
  return render_template('pages/table/tbl_dt-render-column-cells.html')

@blueprint.route('/table/column-manipulation/')
def column_manipulation():
  return render_template('pages/table/tbl_dt-column-manipulation.html')

@blueprint.route('/table/datetime-sorting/')
def datetime_sorting():
  return render_template('pages/table/tbl_dt-datetime-sorting.html')

@blueprint.route('/table/methods/')
def methods():
  return render_template('pages/table/tbl_dt-methods.html')

@blueprint.route('/table/add-rows/')
def add_rows():
  return render_template('pages/table/tbl_dt-add-rows.html')

@blueprint.route('/table/fetch-api/')
def fetch_api():
  return render_template('pages/table/tbl_dt-fetch-api.html')

@blueprint.route('/table/filter/')
def filters():
  return render_template('pages/table/tbl_dt-filters.html')

@blueprint.route('/table/export/')
def export():
  return render_template('pages/table/tbl_dt-export.html')

# Data Table
@blueprint.route('/table/advance-initialization/')
def advance_initialization():
  return render_template('pages/table/dt_advance.html')

@blueprint.route('/table/advance-styling/')
def advance_styling():
  return render_template('pages/table/dt_styling.html')

@blueprint.route('/table/advance-api/')
def advance_api():
  return render_template('pages/table/dt_api.html')

@blueprint.route('/table/advance-plugin/')
def advance_plugin():
  return render_template('pages/table/dt_plugin.html')

@blueprint.route('/table/advance-data-source/')
def advance_data_source():
  return render_template('pages/table/dt_sources.html')

# DT Extension
@blueprint.route('/table/autofill/')
def autofill():
  return render_template('pages/table/dt_ext_autofill.html')

@blueprint.route('/table/basic-button/')
def basic_button():
  return render_template('pages/table/dt_ext_basic_buttons.html')

@blueprint.route('/table/data-export/')
def data_export():
  return render_template('pages/table/dt_ext_export_buttons.html')

@blueprint.route('/table/col-reorder/')
def col_reorder():
  return render_template('pages/table/dt_ext_col_reorder.html')

@blueprint.route('/table/fixed-column/')
def fixed_column():
  return render_template('pages/table/dt_ext_fixed_columns.html')

@blueprint.route('/table/fixed-header/')
def fixed_header():
  return render_template('pages/table/dt_ext_fixed_header.html')

@blueprint.route('/table/key-table/')
def key_table():
  return render_template('pages/table/dt_ext_key_table.html')

@blueprint.route('/table/responsive/')
def responsive():
  return render_template('pages/table/dt_ext_responsive.html')

@blueprint.route('/table/row-reorder/')
def row_reorder():
  return render_template('pages/table/dt_ext_row_reorder.html')

@blueprint.route('/table/scroller/')
def scroller():
  return render_template('pages/table/dt_ext_scroller.html')

@blueprint.route('/table/select-table/')
def select_table():
  return render_template('pages/table/dt_ext_select.html')

# Authentication

######## Start v1 #########
@blueprint.route('/accounts/register-v1/')
def register_v1():
  return render_template('accounts/register-v1.html')

@blueprint.route('/accounts/login-v1/')
def login_v1():
    return render_template('accounts/login-v1.html')

@blueprint.route('/accounts/forgot-password-v1/')
def forgot_password_v1():
  return render_template('accounts/forgot-password-v1.html')

@blueprint.route('/accounts/reset-password-v1/')
def reset_password_v1():
  return render_template('accounts/reset-password-v1.html')

@blueprint.route('/accounts/check-mail-v1/')
def check_mail_v1():
  return render_template('accounts/check-mail-v1.html')

@blueprint.route('/accounts/code-verification-v1/')
def code_verification_v1():
  return render_template('accounts/code-verification-v1.html')

######## End v1 #########


######## Start v2 #########
@blueprint.route('/accounts/register-v2/')
def register_v2():
  return render_template('accounts/register-v2.html')

@blueprint.route('/accounts/login-v2/')
def login_v2():
    return render_template('accounts/login-v2.html')

@blueprint.route('/accounts/forgot-password-v2/')
def forgot_password_v2():
  return render_template('accounts/forgot-password-v2.html')

@blueprint.route('/accounts/reset-password-v2/')
def reset_password_v2():
  return render_template('accounts/reset-password-v2.html')

@blueprint.route('/accounts/check-mail-v2/')
def check_mail_v2():
  return render_template('accounts/check-mail-v2.html')

@blueprint.route('/accounts/code-verification-v2/')
def code_verification_v2():
  return render_template('accounts/code-verification-v2.html')

######## End v2 #########


######## Start v3 #########
@blueprint.route('/accounts/register-v3/')
def register_v3():
  return render_template('accounts/register-v3.html')

@blueprint.route('/accounts/login-v3/')
def login_v3():
    return render_template('accounts/login-v3.html')

@blueprint.route('/accounts/forgot-password-v3/')
def forgot_password_v3():
  return render_template('accounts/forgot-password-v3.html')

@blueprint.route('/accounts/reset-password-v3/')
def reset_password_v3():
  return render_template('accounts/reset-password-v3.html')

@blueprint.route('/accounts/check-mail-v3/')
def check_mail_v3():
  return render_template('accounts/check-mail-v3.html')

@blueprint.route('/accounts/code-verification-v3/')
def code_verification_v3():
  return render_template('accounts/code-verification-v3.html')

######## End v3 #########

# Price
@blueprint.route('/price/price-v1/')
def price_v1():
  return render_template('accounts/price-v1.html')

@blueprint.route('/price/price-v2/')
def price_v2():
  return render_template('accounts/price-v2.html')

# Maintenance
@blueprint.route('/pages/error-404/')
def error_404():
  return render_template('accounts/error-404.html')

@blueprint.route('/pages/coming-soon-v1/')
def coming_soon_v1():
  return render_template('accounts/coming-soon-v1.html')

@blueprint.route('/pages/coming-soon-v2/')
def coming_soon_v2():
  return render_template('accounts/coming-soon-v2.html')

@blueprint.route('/pages/under-contruction/')
def under_construction():
  return render_template('accounts/under-construction.html')

@blueprint.route('/pages/contact-us/')
def contact_us():
  return render_template('accounts/contact-us.html')

@blueprint.route('/pages/faq/')
def faq():
  return render_template('accounts/faq.html')

@blueprint.route('/pages/privacy-policy/')
def privacy_policy():
  return render_template('accounts/privacy-policy.html')

@blueprint.route('/pages/landing/')
def landing():
  return render_template('accounts/landing.html')

@blueprint.route('/other/sample-page/')
def sample_page():
  return render_template('pages/other/sample-page.html')

def get_segment( request ): 
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'
        return segment    
    except:
        return None  
