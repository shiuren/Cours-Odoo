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

# Add a menu between models
### Premièrement repérer le model où vous voulez ajouter les menu; dans mon cas j'ai choisi le point de vente par exemple. Trouver l'id parent à partir de l'indice menuitem, on pourrait voir quelque chose comme ceci : 

        <menuitem
        id="menu_point_root"
        name="Point of Sale"
        groups="group_pos_manager,group_pos_user"
        web_icon="point_of_sale,static/description/icon.png"
        sequence="50"/>
### ici j'ai trouver id="menu_point_root" qui signifie qu'il appartient au menu principale du point de vente

# Introduction des models vente et achat en tant que menu
### Création de record et menuitem

<?xml version="1.0" encoding="utf-8"?>
<odoo>

   <record id="mtx_action_purchase_order" model="ir.actions.act_window">
        <field name="name">Achat</field>
        <field name="res_model">purchase.order</field>
        <field name="view_mode">tree,form</field>
   </record>

 <record id="mtx_action_sale_order" model="ir.actions.act_window">
    <field name="name">Achat</field>
    <field name="res_model">sale.order</field>
    <field name="view_mode">tree,form</field>
 </record>

   <menuitem id="menu_pos_purchacse_settings"
        name="Achat"
        parent="point_of_sale.menu_point_root"
        action="mtx_action_purchase_order"
        groups="base.group_system"/>

   <menuitem id="menu_pos_sale_settings"
        name="Vente"
        parent="point_of_sale.menu_point_root"
        action="mtx_action_sale_order"
        groups="base.group_system"/>

</odoo>


# mtx_project_security lecture seul
### Pour rendre des champs en lecture seul voici un extrait de code python ainsi que son code xml : 

is_readonly = fields.Boolean(compute="_compute_readonly_fields", string="test")


@api.depends('allocated_hours', 'date_deadline')
def _compute_readonly_fields(self):
    for record in self:
       record.is_readonly = self.env["res.users"].has_group('mtx_project_security.group_readonly')




<?xml version='1.0' encoding='utf-8'?>
<odoo>
    <record model="ir.ui.view" id="view_task_form2_inherited">
        <field name="name">project.task.form.inherited</field>
        <field name="model">project.task</field>
        <field name="inherit_id" ref="project.view_task_form2" />
        <field name="arch" type="xml">
            <xpath expr="//form" position="after">
                <field name="is_readonly" invisible='1'/>
            </xpath>
            <xpath expr="//field[@name='date_deadline']" position="attributes">
                <attribute name="readonly">is_readonly</attribute>
            </xpath>
            <xpath expr="//field[@name='allocated_hours']" position="attributes">
                <attribute name="readonly">is_readonly</attribute>
            </xpath>
        </field>     
    </record>

</odoo>

# Dans cette méthode nous avons créé un nouveau champ appelé is_readonly qui est un bolean; son rôle de savoir si l'utilisateur actuel appartient au groupe de sécurité.
# self : c'est un ensemble d'enregistrement de l'objet sur laquel la méthode est appelée
# self.env[''] : Cette syntaxe est utilisée pour accéder à l'objet modèle associé à la table de base de données ici notre modéle est res.user
# dans le fichier xml j'ai mis is_readonly dans le xpath "from" position = "inside" mais invisible ainsi vous pouvez ajoutez tous les champs qui si trouve en mode lecture seul 
