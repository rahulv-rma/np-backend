import { FunctionComponent, useMemo } from 'react';

import { useNPConfig } from '@/contexts/npConfig';

import Tabs from './_components/tabs';

const SelectProducts: FunctionComponent = () => {
  const { config } = useNPConfig();

  const currentWizardStep = config?.currentWizardStep || '-1';

  const organizationId = useMemo(() => {
    return config?.data
      ? JSON.parse(config?.data.replace(/&quot;/g, '"') || '{}')
          ?.organization_id || null
      : null;
  }, [config]);

  const employeeGroups = useMemo(() => {
    return config?.data
      ? JSON.parse(config?.data.replace(/&quot;/g, '"') || '{}')
          ?.employee_groups || []
      : [];
  }, [config]);

  const tabs = useMemo(() => {
    return employeeGroups.map(
      (employee_group: { name: string; budget: number }, index: number) => ({
        label: employee_group?.name,
        idx: index,
        key: index,
        budget: employee_group.budget,
      }),
    );
  }, [employeeGroups]);

  return (
    <div className="grid grid-cols-1 divide-y w-full h-full">
      <Tabs organizationId={organizationId} tabs={tabs} />
      <table>
        <input
          type="hidden"
          name="campaign_creation_wizard-current_step"
          value={currentWizardStep}
          id="id_campaign_creation_wizard-current_step"
        />
        <input
          type="hidden"
          name={`${currentWizardStep}-TOTAL_FORMS`}
          value={employeeGroups.length}
          id={`id_${currentWizardStep}-TOTAL_FORMS`}
        />
        <input
          type="hidden"
          name={`${currentWizardStep}-INITIAL_FORMS`}
          value="0"
          id={`id_${currentWizardStep}-INITIAL_FORMS`}
        />
        <input
          type="hidden"
          name={`${currentWizardStep}-MIN_NUM_FORMS`}
          value="1"
          id={`id_${currentWizardStep}-MIN_NUM_FORMS`}
        />
        <input
          type="hidden"
          name={`${currentWizardStep}-MAX_NUM_FORMS`}
          value="1000"
          id={`id_${currentWizardStep}-MAX_NUM_FORMS`}
        />
      </table>
    </div>
  );
};

export default SelectProducts;