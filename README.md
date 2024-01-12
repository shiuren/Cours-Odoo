# My readme

## Raport
### Pour ajouter un papier format de raport Odoo
    <!-- PAPERFORMAT -->
    <record id="estate_property_paperformat" model="report.paperformat">
        <field name="name">Format Estate Property A4</field>
        <field name="default" eval="False"/>
        <field name="disable_shrinking" eval="True"/>
        <field name="format">A4</field>
        <field name="page_height">0</field>
        <field name="page_width">0</field>
        <field name="orientation">Portrait</field>
        <field name="margin_top">10</field>
        <field name="margin_bottom">10</field>
        <field name="margin_left">5</field>
        <field name="margin_right">5</field>
        <field name="dpi">96</field>
    </record>

### Pour faire une action report

    <!-- ACTION REPORT PFD -->
    <record id="estate_property_report_action" model="ir.actions.report">
        <field name="name">Raport Estate Property</field>
        <field name="model">estate.property</field>
        <field name="report_type">qweb-pdf</field>
        <field name="report_name">estate.template_raport_estate_property</field>
        <field name="report_file">estate.template_raport_estate_property</field>
        <field name="print_report_name">(object.name)</field>
        <field name="binding_model_id" ref="model_estate_property"/>
        <field name="binding_type">report</field>
         <field name="paperformat_id" ref="estate_property_paperformat"/>
    </record>
####  <field name="binding_model_id" ref="model_estate_property"/> => signification : model_ ne change pas estate_property => nom du model: estate.property 

### Pour faire un template

    <!-- TEMPLATE RAPORT ESTATE -->
    <template id="template_raport_estate_property">
        <t t-call="web.html_container">
            <t t-foreach="docs" t-as="doc">
                <div class="page">
                    <p><t t-esc="doc.expected_price"/></p>
                </div>
            </t>
        </t>
    </template>