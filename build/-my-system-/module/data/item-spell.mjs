import mysystemItemBase from './base-item.mjs';

export default class mysystemSpell extends mysystemItemBase {
  static LOCALIZATION_PREFIXES = [
    '_MY_SYSTEM_.Item.base',
    '_MY_SYSTEM_.Item.Spell',
  ];

  static defineSchema() {
    const fields = foundry.data.fields;
    const schema = super.defineSchema();

    schema.spellLevel = new fields.NumberField({
      required: true,
      nullable: false,
      integer: true,
      initial: 1,
      min: 1,
      max: 9,
    });

    return schema;
  }
}
