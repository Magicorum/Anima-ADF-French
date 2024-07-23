import AnimaItemBase from './base-item.mjs';

export default class AnimaSpell extends AnimaItemBase {
  static LOCALIZATION_PREFIXES = [
    'ANIMA.Item.base',
    'ANIMA.Item.Spell',
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
